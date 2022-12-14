# moteaf-lang
Use case example motif: ["Holy Ballin" - Sunday Service Choir](https://www.youtube.com/watch?v=TfpiHv1kP5E)
```python
from moteaf import motif_parse

motif ="""
Am9[0 1 2 3 4 :: 3]-(3/2), 
Bm7[3 4 5 6 :: 3]-(3/2), 
Cmaj9[0 1 2 3 4 :: 5]-(2), 
Em7<[3 5]-(3/4), [6]-(1/4), [7 9]-(1/4), [8]-(1/4), [6]-(1/4) :: 4>, 
Em7<[3]-(1/4), [2]-(1/4), [3]-(1/4), [4]-(1/4), [1]-(1/4) :: 4>
"""

print(motif_parse(motif))
```
Output: 
```python
{'motif': [{'full_chord': {'duration': 1.5,
                           'grid': {'grid_form': 'm9',
                                    'key': {'key_letter': 'A',
                                            'key_symbol': None}},
                           'int_list': [0, 1, 2, 3, 4],
                           'octave': 3}},
           {'full_chord': {'duration': 1.5,
                           'grid': {'grid_form': 'm7',
                                    'key': {'key_letter': 'B',
                                            'key_symbol': None}},
                           'int_list': [3, 4, 5, 6],
                           'octave': 3}},
           {'full_chord': {'duration': 2.0,
                           'grid': {'grid_form': 'maj9',
                                    'key': {'key_letter': 'C',
                                            'key_symbol': None}},
                           'int_list': [0, 1, 2, 3, 4],
                           'octave': 5}},
           {'broken_chord': {'bk_elements': [{'duration': 0.75,
                                              'int_list': [3, 5]},
                                             {'duration': 0.25,
                                              'int_list': [6]},
                                             {'duration': 0.25,
                                              'int_list': [7, 9]},
                                             {'duration': 0.25,
                                              'int_list': [8]},
                                             {'duration': 0.25,
                                              'int_list': [6]}],
                             'grid': {'grid_form': 'm7',
                                      'key': {'key_letter': 'E',
                                              'key_symbol': None}},
                             'octave': 4}},
           {'broken_chord': {'bk_elements': [{'duration': 0.25,
                                              'int_list': [3]},
                                             {'duration': 0.25,
                                              'int_list': [2]},
                                             {'duration': 0.25,
                                              'int_list': [3]},
                                             {'duration': 0.25,
                                              'int_list': [4]},
                                             {'duration': 0.25,
                                              'int_list': [1]}],
                             'grid': {'grid_form': 'm7',
                                      'key': {'key_letter': 'E',
                                              'key_symbol': None}},
                             'octave': 4}}]}
```