from .motif_parser import motif_parse
from .util import get_key_number, ParsedChord
from .motif2midi import motif_2_midi, save_midi
import math

def transpose_motif(motif_tree: dict, transpose: int):
    ''' Returns the transposed motif syntax tree
    '''
    chords = motif_tree['motif']
    for chord in chords:
        chord_dict = chord['full_chord'] if 'full_chord' in chord else chord['broken_chord']
        pc = ParsedChord(chord_dict)
        new_key_num = pc.get_key_number() + transpose
        new_octave = math.floor(new_key_num / 12) + pc.get_octave()
        pc.set_octave(new_octave)
        pc.set_key(new_key_num)
    
    return motif_tree