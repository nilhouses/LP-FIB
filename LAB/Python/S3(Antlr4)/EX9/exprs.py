# Driver que fa de compilador
from antlr4 import *
from exprsLexer import exprsLexer
from exprsParser import exprsParser
from EvalVisitor import EvalVisitor #classe EvalVisitor

input_stream = StdinStream() #llegir de stdin
lexer = exprsLexer(input_stream)
lexer.removeErrorListeners()
token_stream = CommonTokenStream(lexer)
parser = exprsParser(token_stream)
parser.removeErrorListeners()
tree = parser.root()

if parser.getNumberOfSyntaxErrors() == 0:
    visitor = EvalVisitor()
    visitor.visit(tree)
else:
    print(parser.getNumberOfSyntaxErrors(), 'errors de sintaxi.')
    print(tree.toStringTree(recog=parser))