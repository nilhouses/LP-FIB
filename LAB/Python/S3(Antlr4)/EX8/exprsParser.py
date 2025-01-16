# Generated from exprs.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,27,115,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,0,1,0,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,5,2,38,8,2,10,2,12,2,41,9,
        2,3,2,43,8,2,1,3,1,3,1,3,1,3,1,4,5,4,50,8,4,10,4,12,4,53,9,4,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,70,8,
        5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,5,8,88,8,8,10,8,12,8,91,9,8,3,8,93,8,8,1,8,3,8,96,8,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,110,8,8,10,8,12,8,113,
        9,8,1,8,0,1,16,9,0,2,4,6,8,10,12,14,16,0,3,1,0,15,16,1,0,17,18,1,
        0,19,24,121,0,21,1,0,0,0,2,26,1,0,0,0,4,42,1,0,0,0,6,44,1,0,0,0,
        8,51,1,0,0,0,10,69,1,0,0,0,12,71,1,0,0,0,14,75,1,0,0,0,16,95,1,0,
        0,0,18,20,3,2,1,0,19,18,1,0,0,0,20,23,1,0,0,0,21,19,1,0,0,0,21,22,
        1,0,0,0,22,24,1,0,0,0,23,21,1,0,0,0,24,25,3,6,3,0,25,1,1,0,0,0,26,
        27,5,1,0,0,27,28,5,26,0,0,28,29,5,2,0,0,29,30,3,4,2,0,30,31,5,3,
        0,0,31,32,3,8,4,0,32,33,5,4,0,0,33,3,1,0,0,0,34,39,5,26,0,0,35,36,
        5,5,0,0,36,38,5,26,0,0,37,35,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,
        39,40,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,42,34,1,0,0,0,42,43,1,
        0,0,0,43,5,1,0,0,0,44,45,5,6,0,0,45,46,3,8,4,0,46,47,5,4,0,0,47,
        7,1,0,0,0,48,50,3,10,5,0,49,48,1,0,0,0,50,53,1,0,0,0,51,49,1,0,0,
        0,51,52,1,0,0,0,52,9,1,0,0,0,53,51,1,0,0,0,54,55,5,26,0,0,55,56,
        5,7,0,0,56,70,3,16,8,0,57,58,5,8,0,0,58,70,3,16,8,0,59,60,5,9,0,
        0,60,61,3,16,8,0,61,62,3,12,6,0,62,70,1,0,0,0,63,64,5,10,0,0,64,
        65,3,16,8,0,65,66,3,14,7,0,66,70,1,0,0,0,67,68,5,11,0,0,68,70,3,
        16,8,0,69,54,1,0,0,0,69,57,1,0,0,0,69,59,1,0,0,0,69,63,1,0,0,0,69,
        67,1,0,0,0,70,11,1,0,0,0,71,72,5,12,0,0,72,73,3,8,4,0,73,74,5,4,
        0,0,74,13,1,0,0,0,75,76,5,13,0,0,76,77,3,8,4,0,77,78,5,4,0,0,78,
        15,1,0,0,0,79,80,6,8,-1,0,80,96,5,25,0,0,81,96,5,26,0,0,82,83,5,
        26,0,0,83,92,5,2,0,0,84,89,3,16,8,0,85,86,5,5,0,0,86,88,3,16,8,0,
        87,85,1,0,0,0,88,91,1,0,0,0,89,87,1,0,0,0,89,90,1,0,0,0,90,93,1,
        0,0,0,91,89,1,0,0,0,92,84,1,0,0,0,92,93,1,0,0,0,93,94,1,0,0,0,94,
        96,5,3,0,0,95,79,1,0,0,0,95,81,1,0,0,0,95,82,1,0,0,0,96,111,1,0,
        0,0,97,98,10,7,0,0,98,99,5,14,0,0,99,110,3,16,8,7,100,101,10,6,0,
        0,101,102,7,0,0,0,102,110,3,16,8,7,103,104,10,5,0,0,104,105,7,1,
        0,0,105,110,3,16,8,6,106,107,10,4,0,0,107,108,7,2,0,0,108,110,3,
        16,8,5,109,97,1,0,0,0,109,100,1,0,0,0,109,103,1,0,0,0,109,106,1,
        0,0,0,110,113,1,0,0,0,111,109,1,0,0,0,111,112,1,0,0,0,112,17,1,0,
        0,0,113,111,1,0,0,0,10,21,39,42,51,69,89,92,95,109,111
    ]

class exprsParser ( Parser ):

    grammarFileName = "exprs.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'function'", "'('", "')'", "'end'", "','", 
                     "'main'", "':='", "'write'", "'if'", "'while'", "'return'", 
                     "'then'", "'do'", "'^'", "'/'", "'*'", "'+'", "'-'", 
                     "'<'", "'<='", "'>'", "'>='", "'='", "'<>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "DIV", "MUL", 
                      "SUM", "RES", "MENOR", "MENORIGUAL", "MAJOR", "MAJORIGUAL", 
                      "IGUAL", "DIFERENT", "NUM", "VAR", "WS" ]

    RULE_root = 0
    RULE_functionDeclaration = 1
    RULE_paramList = 2
    RULE_main = 3
    RULE_statements = 4
    RULE_statement = 5
    RULE_cosIf = 6
    RULE_cosWhile = 7
    RULE_expr = 8

    ruleNames =  [ "root", "functionDeclaration", "paramList", "main", "statements", 
                   "statement", "cosIf", "cosWhile", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    DIV=15
    MUL=16
    SUM=17
    RES=18
    MENOR=19
    MENORIGUAL=20
    MAJOR=21
    MAJORIGUAL=22
    IGUAL=23
    DIFERENT=24
    NUM=25
    VAR=26
    WS=27

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def main(self):
            return self.getTypedRuleContext(exprsParser.MainContext,0)


        def functionDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprsParser.FunctionDeclarationContext)
            else:
                return self.getTypedRuleContext(exprsParser.FunctionDeclarationContext,i)


        def getRuleIndex(self):
            return exprsParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = exprsParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 18
                self.functionDeclaration()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
            self.main()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(exprsParser.VAR, 0)

        def paramList(self):
            return self.getTypedRuleContext(exprsParser.ParamListContext,0)


        def statements(self):
            return self.getTypedRuleContext(exprsParser.StatementsContext,0)


        def getRuleIndex(self):
            return exprsParser.RULE_functionDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDeclaration" ):
                return visitor.visitFunctionDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def functionDeclaration(self):

        localctx = exprsParser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_functionDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(exprsParser.T__0)
            self.state = 27
            self.match(exprsParser.VAR)
            self.state = 28
            self.match(exprsParser.T__1)
            self.state = 29
            self.paramList()
            self.state = 30
            self.match(exprsParser.T__2)
            self.state = 31
            self.statements()
            self.state = 32
            self.match(exprsParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self, i:int=None):
            if i is None:
                return self.getTokens(exprsParser.VAR)
            else:
                return self.getToken(exprsParser.VAR, i)

        def getRuleIndex(self):
            return exprsParser.RULE_paramList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = exprsParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 34
                self.match(exprsParser.VAR)
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==5:
                    self.state = 35
                    self.match(exprsParser.T__4)
                    self.state = 36
                    self.match(exprsParser.VAR)
                    self.state = 41
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statements(self):
            return self.getTypedRuleContext(exprsParser.StatementsContext,0)


        def getRuleIndex(self):
            return exprsParser.RULE_main

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain" ):
                return visitor.visitMain(self)
            else:
                return visitor.visitChildren(self)




    def main(self):

        localctx = exprsParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_main)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(exprsParser.T__5)
            self.state = 45
            self.statements()
            self.state = 46
            self.match(exprsParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprsParser.StatementContext)
            else:
                return self.getTypedRuleContext(exprsParser.StatementContext,i)


        def getRuleIndex(self):
            return exprsParser.RULE_statements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements" ):
                return visitor.visitStatements(self)
            else:
                return visitor.visitChildren(self)




    def statements(self):

        localctx = exprsParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 67112704) != 0):
                self.state = 48
                self.statement()
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return exprsParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CondwhileContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(exprsParser.ExprContext,0)

        def cosWhile(self):
            return self.getTypedRuleContext(exprsParser.CosWhileContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondwhile" ):
                return visitor.visitCondwhile(self)
            else:
                return visitor.visitChildren(self)


    class CondicionalContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(exprsParser.ExprContext,0)

        def cosIf(self):
            return self.getTypedRuleContext(exprsParser.CosIfContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicional" ):
                return visitor.visitCondicional(self)
            else:
                return visitor.visitChildren(self)


    class WriteContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(exprsParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrite" ):
                return visitor.visitWrite(self)
            else:
                return visitor.visitChildren(self)


    class AsignarContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(exprsParser.VAR, 0)
        def expr(self):
            return self.getTypedRuleContext(exprsParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignar" ):
                return visitor.visitAsignar(self)
            else:
                return visitor.visitChildren(self)


    class ReturnContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(exprsParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn" ):
                return visitor.visitReturn(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = exprsParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_statement)
        try:
            self.state = 69
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                localctx = exprsParser.AsignarContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.match(exprsParser.VAR)
                self.state = 55
                self.match(exprsParser.T__6)
                self.state = 56
                self.expr(0)
                pass
            elif token in [8]:
                localctx = exprsParser.WriteContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.match(exprsParser.T__7)
                self.state = 58
                self.expr(0)
                pass
            elif token in [9]:
                localctx = exprsParser.CondicionalContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 59
                self.match(exprsParser.T__8)
                self.state = 60
                self.expr(0)
                self.state = 61
                self.cosIf()
                pass
            elif token in [10]:
                localctx = exprsParser.CondwhileContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 63
                self.match(exprsParser.T__9)
                self.state = 64
                self.expr(0)
                self.state = 65
                self.cosWhile()
                pass
            elif token in [11]:
                localctx = exprsParser.ReturnContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 67
                self.match(exprsParser.T__10)
                self.state = 68
                self.expr(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CosIfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statements(self):
            return self.getTypedRuleContext(exprsParser.StatementsContext,0)


        def getRuleIndex(self):
            return exprsParser.RULE_cosIf

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCosIf" ):
                return visitor.visitCosIf(self)
            else:
                return visitor.visitChildren(self)




    def cosIf(self):

        localctx = exprsParser.CosIfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_cosIf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(exprsParser.T__11)
            self.state = 72
            self.statements()
            self.state = 73
            self.match(exprsParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CosWhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statements(self):
            return self.getTypedRuleContext(exprsParser.StatementsContext,0)


        def getRuleIndex(self):
            return exprsParser.RULE_cosWhile

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCosWhile" ):
                return visitor.visitCosWhile(self)
            else:
                return visitor.visitChildren(self)




    def cosWhile(self):

        localctx = exprsParser.CosWhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_cosWhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(exprsParser.T__12)
            self.state = 76
            self.statements()
            self.state = 77
            self.match(exprsParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return exprsParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NumeroContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(exprsParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumero" ):
                return visitor.visitNumero(self)
            else:
                return visitor.visitChildren(self)


    class VariableContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(exprsParser.VAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)


    class OpLogicContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprsParser.ExprContext)
            else:
                return self.getTypedRuleContext(exprsParser.ExprContext,i)

        def MENOR(self):
            return self.getToken(exprsParser.MENOR, 0)
        def MENORIGUAL(self):
            return self.getToken(exprsParser.MENORIGUAL, 0)
        def MAJOR(self):
            return self.getToken(exprsParser.MAJOR, 0)
        def MAJORIGUAL(self):
            return self.getToken(exprsParser.MAJORIGUAL, 0)
        def IGUAL(self):
            return self.getToken(exprsParser.IGUAL, 0)
        def DIFERENT(self):
            return self.getToken(exprsParser.DIFERENT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpLogic" ):
                return visitor.visitOpLogic(self)
            else:
                return visitor.visitChildren(self)


    class FuncCallContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(exprsParser.VAR, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprsParser.ExprContext)
            else:
                return self.getTypedRuleContext(exprsParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCall" ):
                return visitor.visitFuncCall(self)
            else:
                return visitor.visitChildren(self)


    class OpAritContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprsParser.ExprContext)
            else:
                return self.getTypedRuleContext(exprsParser.ExprContext,i)

        def MUL(self):
            return self.getToken(exprsParser.MUL, 0)
        def DIV(self):
            return self.getToken(exprsParser.DIV, 0)
        def SUM(self):
            return self.getToken(exprsParser.SUM, 0)
        def RES(self):
            return self.getToken(exprsParser.RES, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpArit" ):
                return visitor.visitOpArit(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = exprsParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = exprsParser.NumeroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 80
                self.match(exprsParser.NUM)
                pass

            elif la_ == 2:
                localctx = exprsParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 81
                self.match(exprsParser.VAR)
                pass

            elif la_ == 3:
                localctx = exprsParser.FuncCallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 82
                self.match(exprsParser.VAR)
                self.state = 83
                self.match(exprsParser.T__1)
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==25 or _la==26:
                    self.state = 84
                    self.expr(0)
                    self.state = 89
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==5:
                        self.state = 85
                        self.match(exprsParser.T__4)
                        self.state = 86
                        self.expr(0)
                        self.state = 91
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 94
                self.match(exprsParser.T__2)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 111
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 109
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = exprsParser.OpAritContext(self, exprsParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 97
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 98
                        self.match(exprsParser.T__13)
                        self.state = 99
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = exprsParser.OpAritContext(self, exprsParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 100
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 101
                        _la = self._input.LA(1)
                        if not(_la==15 or _la==16):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 102
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = exprsParser.OpAritContext(self, exprsParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 103
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 104
                        _la = self._input.LA(1)
                        if not(_la==17 or _la==18):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 105
                        self.expr(6)
                        pass

                    elif la_ == 4:
                        localctx = exprsParser.OpLogicContext(self, exprsParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 106
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 107
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 33030144) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 108
                        self.expr(5)
                        pass

             
                self.state = 113
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[8] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         




