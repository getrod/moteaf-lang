from moteaf import motif_parse, motif_2_midi, save_midi

motif ="""
Am9[0 1 2 3 4 :: 4]-(3/2), 
Bm7[3 4 5 6 :: 3]-(3/2), 
Cmaj9[0 1 2 3 4 :: 5]-(2), 
Em7<[3 5]-(3/4), [6]-(1/4), [7 9]-(1/4), [8]-(1/4), [6]-(1/4) :: 4>, 
Em7<[3]-(1/4), [2]-(1/4), [3]-(1/4), [4]-(1/4), [1]-(1/4) :: 4>
"""

motif_tree = motif_parse(motif)
midi = motif_2_midi(motif_tree)
save_midi(midi, 'ballin.mid')