# Generated from exprs.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .exprsParser import exprsParser
else:
    from exprsParser import exprsParser

# This class defines a complete listener for a parse tree produced by exprsParser.
class exprsListener(ParseTreeListener):

    # Enter a parse tree produced by exprsParser#root.
    def enterRoot(self, ctx:exprsParser.RootContext):
        pass

    # Exit a parse tree produced by exprsParser#root.
    def exitRoot(self, ctx:exprsParser.RootContext):
        pass


    # Enter a parse tree produced by exprsParser#suma.
    def enterSuma(self, ctx:exprsParser.SumaContext):
        pass

    # Exit a parse tree produced by exprsParser#suma.
    def exitSuma(self, ctx:exprsParser.SumaContext):
        pass


    # Enter a parse tree produced by exprsParser#potencia.
    def enterPotencia(self, ctx:exprsParser.PotenciaContext):
        pass

    # Exit a parse tree produced by exprsParser#potencia.
    def exitPotencia(self, ctx:exprsParser.PotenciaContext):
        pass


    # Enter a parse tree produced by exprsParser#numero.
    def enterNumero(self, ctx:exprsParser.NumeroContext):
        pass

    # Exit a parse tree produced by exprsParser#numero.
    def exitNumero(self, ctx:exprsParser.NumeroContext):
        pass


    # Enter a parse tree produced by exprsParser#multiplicacio.
    def enterMultiplicacio(self, ctx:exprsParser.MultiplicacioContext):
        pass

    # Exit a parse tree produced by exprsParser#multiplicacio.
    def exitMultiplicacio(self, ctx:exprsParser.MultiplicacioContext):
        pass


    # Enter a parse tree produced by exprsParser#resta.
    def enterResta(self, ctx:exprsParser.RestaContext):
        pass

    # Exit a parse tree produced by exprsParser#resta.
    def exitResta(self, ctx:exprsParser.RestaContext):
        pass


    # Enter a parse tree produced by exprsParser#divisio.
    def enterDivisio(self, ctx:exprsParser.DivisioContext):
        pass

    # Exit a parse tree produced by exprsParser#divisio.
    def exitDivisio(self, ctx:exprsParser.DivisioContext):
        pass



del exprsParser