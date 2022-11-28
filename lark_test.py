from lark import Lark
json_parser = Lark(r"""
    value: dict
         | list
         | ESCAPED_STRING   ->  string
         | SIGNED_NUMBER    ->  number
         | "true"           ->  bool
         | "false"          ->  bool
         | "null"           ->  null

    list : "[" [value ("," value)*] "]"

    dict : "{" [pair ("," pair)*] "}"
    pair : ESCAPED_STRING ":" value

    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS
    %ignore WS

    """, start='value')

text = '{"key": ["item0", "item1", 3.14, false]}'
parsed = json_parser.parse(text)
print(parsed)

print(parsed.pretty())