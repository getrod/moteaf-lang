from lark import Lark
from lark import Transformer

f = open('motif_parser.lark')
motif_parser = Lark(f.read(), start='motif')

class TreeToJson(Transformer):
    def motif(self, mtf):
        _motif = []
        for elem in mtf:
            _motif.append(elem)
        return {'motif':_motif}

    def element(self, elem):
        return elem[0]

    def broken_chord(self, bk_c):
        grid = bk_c[0]
        octave = bk_c[len(bk_c)-1]
        bk_elems = bk_c[1:len(bk_c)-1]
        _bk_elems = []
        for bk_elem in bk_elems:
            _bk_elems.append(bk_elem['bk_element'])
        
        bk_dict = dict()
        bk_dict.update(grid)
        bk_dict['bk_elements'] = _bk_elems
        bk_dict['octave'] = octave
        return {'broken_chord': bk_dict}

    def bk_element(self, bke):
        bk_ele = dict()
        bk_ele.update(bke[0])
        bk_ele.update(bke[1])
        return {'bk_element': bk_ele}
    
    def full_chord(self, fch):
        dict_fc = dict()
        dict_fc.update(fch[0])
        dict_fc.update(fch[1])
        dict_fc['octave'] = fch[2]
        dict_fc.update(fch[3])
        return {'full_chord': dict_fc}

    def grid(self, g):
        g_dict = dict()
        for ge in g:
            g_dict.update(ge)
        return {'grid': g_dict}

    def grid_form(self, gf):
        (gf,) = gf
        return {'grid_form': str(gf)}

    def key(self, k):
        k_dict = dict()
        k_dict['key_letter'] = k[0]
        k_dict['key_symbol'] = k[1]
        return {'key': k_dict}

    def key_letter(self, kl):
        (kl,) = kl
        return str(kl)

    def key_symbol(self, ks):
        (ks,) = ks
        return str(ks)

    def int_list(self, lst):
        _int_list = []
        for num in lst:
            _int_list.append(num)
        return {'int_list': _int_list}

    def duration(self, d):
        return {'duration': float(d[0])}
    
    def octave(self, o):
        return int(o[0])

    def int(self, i):
        return int(i[0])

    def uint(self, i):
        return int(i[0])

    def rational(self, nums):
        return nums[0] / nums[1]


def motif_compile(motif_string: str):
    tree = motif_parser.parse(motif_string)
    return TreeToJson().transform(tree)

test ="""Am9[0 1 2 3 4 :: 3]-(3/2),
Bm7[3 4 5 6 :: 3]-(3/2), 
Cmaj9[0 1 2 3 4 :: 5]-(2), 
Em7<[3 5]-(3/4), [6]-(1/4), [7 9]-(1/4), [8]-(1/4), [6]-(1/4) :: 4>, 
F#m7<[3]-(1/4), [2]-(1/4), [3]-(1/4), [4]-(1/4), [1]-(1/4)>"""

print(motif_compile(test))