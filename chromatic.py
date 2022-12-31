from moteaf import motif_parse, motif_2_midi, save_midi

motif ="""
C chrom< [0]-(1/4),[1]-(1/4),[2]-(1/4),[3]-(1/4),[4]-(1/4),[5]-(1/4),[6]-(1/4),[7]-(1/4),[8]-(1/4),[9]-(1/4),[10]-(1/4),[11]-(1/4), [12]-(3/4) :: 5>
"""

motif_tree = motif_parse(motif)
midi = motif_2_midi(motif_tree)
save_midi(midi, 'chrome.mid')