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


    # Visit a parse tree produced by exprsParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:exprsParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#paramListBuida.
    def visitParamListBuida(self, ctx:exprsParser.ParamListBuidaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#paramListPlena.
    def visitParamListPlena(self, ctx:exprsParser.ParamListPlenaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#main.
    def visitMain(self, ctx:exprsParser.MainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#statements.
    def visitStatements(self, ctx:exprsParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#asignar.
    def visitAsignar(self, ctx:exprsParser.AsignarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#write.
    def visitWrite(self, ctx:exprsParser.WriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#condicional.
    def visitCondicional(self, ctx:exprsParser.CondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#condwhile.
    def visitCondwhile(self, ctx:exprsParser.CondwhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#return.
    def visitReturn(self, ctx:exprsParser.ReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#cosIf.
    def visitCosIf(self, ctx:exprsParser.CosIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#cosWhile.
    def visitCosWhile(self, ctx:exprsParser.CosWhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#numero.
    def visitNumero(self, ctx:exprsParser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#variable.
    def visitVariable(self, ctx:exprsParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#opLogic.
    def visitOpLogic(self, ctx:exprsParser.OpLogicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#funcCall.
    def visitFuncCall(self, ctx:exprsParser.FuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#opArit.
    def visitOpArit(self, ctx:exprsParser.OpAritContext):
        return self.visitChildren(ctx)



del exprsParser