# Driver que fa de compilador
from antlr4 import *
from exprsLexer import exprsLexer
from exprsParser import exprsParser
from exprsVisitor import exprsVisitor
from TreeVisitor import TreeVisitor #classe TreeVisitor
from EvalVisitor import EvalVisitor #classe EvalVisitor

input_stream = InputStream(input('? '))
lexer = exprsLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = exprsParser(token_stream)
tree = parser.root()
visitor = TreeVisitor()
visitor = EvalVisitor()
visitor.visit(tree)