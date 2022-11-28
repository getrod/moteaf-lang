'''
Sources:    https://medium.com/100-days-of-algorithms/day-94-earley-parser-3fffdb33edc7
            An introduction to formal languages and automata / Peter Linz.—5th ed

Important Notes:
            - For practical reasons, null chars are not allowed
'''

class Grammar:
    ''' Context Free Grammar '''
    def __init__(self, start_var: str, rules: list[str]):
        self.start_var = start_var
        self.rules = rules

grammar = Grammar('S', [
    'S -> aSa',
    'S -> bSb',
    'S -> #'
])


