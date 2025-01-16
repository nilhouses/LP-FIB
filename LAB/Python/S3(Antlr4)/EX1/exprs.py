#script per testejar exprs.g4

from antlr4 import *
from exprsLexer import exprsLexer
from exprsParser import exprsParser
input_stream = InputStream(input('? '))
lexer = exprsLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = exprsParser(token_stream)
tree = parser.root()
print(tree.toStringTree(recog=parser))
