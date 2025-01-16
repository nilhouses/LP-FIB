# Aquesta classe mostra l'ubicació dels errors sintàctics

from antlr4.error.ErrorListener import ErrorListener

class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"Syntax Error: line {line}, column {column}: {msg}")
