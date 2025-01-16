# Driver que fa de compilador
from antlr4 import *
from exprsLexer import exprsLexer
from exprsParser import exprsParser
from EvalVisitor import EvalVisitor #classe EvalVisitor

input_stream = StdinStream() #llegir de stdin
lexer = exprsLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = exprsParser(token_stream)
tree = parser.root()
visitor = EvalVisitor()
visitor.visit(tree)