from mido import Message, MidiFile, MidiTrack
import math
from .util import Grid, grid_2_chromatic, Midi
from .motif_parser import motif_parse

class MIDI_MESSAGE:
    on = "note_on"
    off = "note_off"

def beat_2_ticks(mid: MidiFile, duration: float):
    return math.floor(mid.ticks_per_beat * duration)

def fullchord_2_midi(fullchord, start_beat: float = 0):
    """Returns both the midi and the ending beat"""
    # get midi notes
    _grid = fullchord["grid"]
    key = _grid["key"]
    notes = fullchord["int_list"]
    octave = fullchord["octave"]
    duration = fullchord["duration"]
    grid = Grid(
        key_letter=key["key_letter"],
        key_symbol=key["key_symbol"],
        form=_grid["grid_form"],
    )
    midi_notes = grid_2_chromatic(grid, notes, octave)

    # make midi messages
    total_beat = start_beat
    midi = []
    for note in midi_notes:
        midi.append(
            Midi(MIDI_MESSAGE.on, note=note, velocity=99, beat=total_beat)
        )
        midi.append(
            Midi(MIDI_MESSAGE.off, note=note, velocity=99, beat=total_beat + duration)
        )
    total_beat += duration

    return midi, total_beat

def brokenchord_2_midi(brokenchord, start_beat: float = 0):
    # get broken chord values
    _grid = brokenchord["grid"]
    key = _grid["key"]
    grid = Grid(
        key_letter=key["key_letter"],
        key_symbol=key["key_symbol"],
        form=_grid["grid_form"],
    )
    octave = brokenchord['octave']

    # get midi messages
    midi = []
    total_beat = start_beat
    bk_elements = brokenchord['bk_elements']
    for bk in bk_elements:
        notes = bk['int_list']
        duration = bk['duration']
        midi_notes = grid_2_chromatic(grid, notes, octave)

        # make midi messages
        for note in midi_notes:
            midi.append(
                Midi(MIDI_MESSAGE.on, note=note, velocity=99, beat=total_beat)
            )
            midi.append(
                Midi(MIDI_MESSAGE.off, note=note, velocity=99, beat=total_beat + duration)
            )
        total_beat += duration
    return midi, total_beat

def absolute_2_relative_time(midi: list[Midi]):
    _midi = list(midi)
    _midi.sort(key= lambda m: m.beat)
    current_beat = 0
    for midi_mess in _midi:
        if midi_mess.beat != current_beat:
            temp = midi_mess.beat
            midi_mess.beat = midi_mess.beat - current_beat
            current_beat = temp
        else:
            midi_mess.beat = 0
    return _midi

def create_midi_track_mido(midi: list[Midi], filename: str):
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    midi = absolute_2_relative_time(midi)

    for midi_event in midi:  
        track.append(
            Message(
                midi_event.event,
                note=midi_event.note,
                velocity=midi_event.velocity,
                time=beat_2_ticks(mid, midi_event.beat),
            )
        )

    mid.save(filename)


def motif_2_midi(motif_tree: dict):
    ''' Takes a motif tree and returns the midi
    '''
    chords = motif_tree["motif"]

    # convert chords to midi
    midi = []
    total_beat = 0
    for chord in chords:
        if 'full_chord' in chord:
            _midi, end_beat = fullchord_2_midi(chord['full_chord'], total_beat)
            midi += _midi
            total_beat = end_beat
        else:
            _midi, end_beat = brokenchord_2_midi(chord['broken_chord'], total_beat)
            midi += _midi
            total_beat = end_beat
    
    return midi

def save_midi(midi: list[Midi], filename: str):
    create_midi_track_mido(midi, filename)
    