import math

key_letters = ["A", "B", "C", "D", "E", "F", "G"]
key_letter_nums = [9, 11, 0, 2, 4, 5, 7]
key_symbols = ["#", "b"]

grid_forms = {
    "maj": [0, 4, 7],
    "m": [0, 3, 7],
    "sus2": [0, 2, 7],
    "sus4": [0, 5, 7],
    "maj7": [0, 4, 7, 11],
    "m7": [0, 3, 7, 10],
    "maj9": [0, 2, 4, 7, 11],
    "m9": [0, 2, 3, 7, 10],
    "chrom": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
}

def get_key_number(key_letter: str, key_symbol: str = None):
    ''' 
    Finds key number associate with the key
    If no key, error
    '''
    idx = 0

    # find key letter
    _match = False
    for i in range(len(key_letters)):
        letter = key_letters[i]
        if letter == key_letter:
            _match = True
            idx = i
            break
    if _match == False: raise Exception(f'No key matches {key_letter}')

    # if key symbol, find it
    if key_symbol != None:
        _match = False
        for sym in key_symbols:
            if sym == key_symbol:
                _match = True
                break
        if _match == False: raise Exception(f'No key symbol {key_symbol}')
    
    # find key number
    key_num = key_letter_nums[idx]
    if key_symbol != None: 
        key_num = key_num + 1 if key_symbol == '#' else key_num - 1 
    key_num = key_num % 12
    return key_num

def get_key_name(key_num: int):
    ''' Returns both the key letter and key symbol '''
    _key_num = key_num % 12
    k_letter = ''
    k_symbol = None
    for i in range(len(key_letter_nums)):
        kn = key_letter_nums[i]
        if _key_num == kn:
            k_letter = key_letters[i]
            return k_letter, None

    # check in between the numbers
    for i in range(len(key_letter_nums)):
        kn_len = len(key_letter_nums)
        if _key_num > key_letter_nums[i % kn_len] and _key_num < key_letter_nums[(i + 1) % kn_len]:
            k_letter = key_letters[i]
            k_symbol = '#'
            return k_letter, k_symbol
    
    raise Exception(f'"get_key_name()" made an error with key: {key_num}')

def _test_get_key_number(): 
    print(get_key_number('C'))
    print(get_key_number('G'))
    print(get_key_number('B'))
    print(get_key_number('Hi'))
    print(get_key_number('C', '#'))
    print(get_key_number('C', 'b'))
    print(get_key_number('B', '#'))
    print(get_key_number('C', '5'))

class Grid:
    def __init__(self, form: str, key_letter: str, key_symbol: str = None):
        self.key_letter = key_letter
        self.key_symbol = key_symbol
        self.form = form

def grid_2_chromatic(grid: Grid, grid_notes: list[int], octave: int = None):
    chromatic_notes = []

    # find the key number
    key_num = get_key_number(grid.key_letter, grid.key_symbol)
    
    # find grid form numbers
    if grid.form not in grid_forms:
        raise Exception(f'Grid form "{grid.form}" not defined')
    grid_nums = list(set(grid_forms[grid.form])) # ensure unique numbers
    grid_nums.sort()

    # transpose grid to key
    for i in range(len(grid_nums)): grid_nums[i] += key_num

    # convert each grid note to chromatic note
    for grid_note in grid_notes:
        chrome_note = grid_nums[grid_note % len(grid_nums)] + (12 * math.floor(grid_note / len(grid_nums)))
        if octave: chrome_note += 12 * octave
        chromatic_notes.append(chrome_note)
    
    return chromatic_notes

def _test_grid_2_chromatic():
    grid = Grid(key_letter='C', key_symbol='#',  form='maj7')
    print(grid_2_chromatic(grid, [-1, 0, 1, 2, 3]))

class Midi:
    def __init__(self, event, note, velocity, beat) -> None:
        self.event = event
        self.note = note
        self.velocity = velocity
        self.beat = beat

    def __str__(self) -> str:
        return f'event: {self.event}, note: {self.note}, velocity: {self.velocity}, beat: {self.beat}'

class ParsedChord:
    def __init__(self, chord) -> None:
        self.chord = chord

    def get_key_number(self):
        k_letter = self.chord["grid"]["key"]["key_letter"]
        k_symbol = self.chord["grid"]["key"]["key_symbol"]
        k_num = get_key_number(k_letter, k_symbol)
        return k_num

    def set_key(self, key_num: int):
        k_letter, k_symbol = get_key_name(key_num)
        self.chord["grid"]["key"]["key_letter"] = k_letter
        self.chord["grid"]["key"]["key_symbol"] = k_symbol

    def get_octave(self):
        return self.chord["octave"]

    def set_octave(self, octave: int):
        self.chord["octave"] = octave