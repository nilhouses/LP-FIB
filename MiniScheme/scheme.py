#Interpreta el fitxer que se li passa com a argument
from antlr4 import *
from schemeLexer import schemeLexer
from schemeParser import schemeParser
from EvalVisitor import EvalVisitor
from MyErrorListener import MyErrorListener # Informa sobre la línia i columna de l'error.
from ex import ex # Excepcions personalitzades
import sys #Per gestionar el usage

if len(sys.argv) < 2:
    print("Usage: python3 scheme.py <program.scm>")
    sys.exit(1)

input_file = sys.argv[1]
input_stream = FileStream(input_file, encoding='utf-8')

lexer = schemeLexer(input_stream)
lexer.removeErrorListeners()
token_stream = CommonTokenStream(lexer)
parser = schemeParser(token_stream)
parser.removeErrorListeners()
parser.addErrorListener(MyErrorListener())
tree = parser.root()

# Errors
if parser.getNumberOfSyntaxErrors() == 0:
    visitor = EvalVisitor()
    try:
        visitor.visit(tree)
    except ex as msg: #Errors personalitzats
       print(msg)
    except Exception as e: #Errors no controlats
       print("ERROR: The program contains semantic, type or execution errors")
else: #Errors sintàctics
    if  parser.getNumberOfSyntaxErrors() == 1:
        print(parser.getNumberOfSyntaxErrors(), 'SyntaxError')
    else:
        print(parser.getNumberOfSyntaxErrors(), 'SyntaxErrors')
    print(tree.toStringTree(recog=parser))
