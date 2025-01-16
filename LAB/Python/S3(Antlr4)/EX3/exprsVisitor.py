# Generated from exprs.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .exprsParser import exprsParser
else:
    from exprsParser import exprsParser

# This class defines a complete generic visitor for a parse tree produced by exprsParser.

class exprsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by exprsParser#root.
    def visitRoot(self, ctx:exprsParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#suma.
    def visitSuma(self, ctx:exprsParser.SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#potencia.
    def visitPotencia(self, ctx:exprsParser.PotenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#numero.
    def visitNumero(self, ctx:exprsParser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#multiplicacio.
    def visitMultiplicacio(self, ctx:exprsParser.MultiplicacioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#resta.
    def visitResta(self, ctx:exprsParser.RestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#divisio.
    def visitDivisio(self, ctx:exprsParser.DivisioContext):
        return self.visitChildren(ctx)



del exprsParser