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
        4,1,21,74,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,1,1,5,1,16,8,1,10,1,12,1,19,9,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,3,2,34,8,2,1,3,1,3,4,3,38,8,3,11,3,12,3,39,
        1,3,1,3,1,4,1,4,4,4,46,8,4,11,4,12,4,47,1,4,1,4,1,5,1,5,1,5,3,5,
        55,8,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,69,8,
        5,10,5,12,5,72,9,5,1,5,0,1,10,6,0,2,4,6,8,10,0,3,1,0,9,10,1,0,11,
        12,1,0,13,18,78,0,12,1,0,0,0,2,17,1,0,0,0,4,33,1,0,0,0,6,35,1,0,
        0,0,8,43,1,0,0,0,10,54,1,0,0,0,12,13,3,2,1,0,13,1,1,0,0,0,14,16,
        3,4,2,0,15,14,1,0,0,0,16,19,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,
        18,3,1,0,0,0,19,17,1,0,0,0,20,21,5,20,0,0,21,22,5,1,0,0,22,34,3,
        10,5,0,23,24,5,2,0,0,24,34,3,10,5,0,25,26,5,3,0,0,26,27,3,10,5,0,
        27,28,3,6,3,0,28,34,1,0,0,0,29,30,5,4,0,0,30,31,3,10,5,0,31,32,3,
        8,4,0,32,34,1,0,0,0,33,20,1,0,0,0,33,23,1,0,0,0,33,25,1,0,0,0,33,
        29,1,0,0,0,34,5,1,0,0,0,35,37,5,5,0,0,36,38,3,4,2,0,37,36,1,0,0,
        0,38,39,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,41,1,0,0,0,41,42,
        5,6,0,0,42,7,1,0,0,0,43,45,5,7,0,0,44,46,3,4,2,0,45,44,1,0,0,0,46,
        47,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,49,1,0,0,0,49,50,5,6,0,
        0,50,9,1,0,0,0,51,52,6,5,-1,0,52,55,5,19,0,0,53,55,5,20,0,0,54,51,
        1,0,0,0,54,53,1,0,0,0,55,70,1,0,0,0,56,57,10,6,0,0,57,58,5,8,0,0,
        58,69,3,10,5,6,59,60,10,5,0,0,60,61,7,0,0,0,61,69,3,10,5,6,62,63,
        10,4,0,0,63,64,7,1,0,0,64,69,3,10,5,5,65,66,10,3,0,0,66,67,7,2,0,
        0,67,69,3,10,5,4,68,56,1,0,0,0,68,59,1,0,0,0,68,62,1,0,0,0,68,65,
        1,0,0,0,69,72,1,0,0,0,70,68,1,0,0,0,70,71,1,0,0,0,71,11,1,0,0,0,
        72,70,1,0,0,0,7,17,33,39,47,54,68,70
    ]

class exprsParser ( Parser ):

    grammarFileName = "exprs.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':='", "'write'", "'if'", "'while'", 
                     "'then'", "'end'", "'do'", "'^'", "'/'", "'*'", "'+'", 
                     "'-'", "'<'", "'<='", "'>'", "'>='", "'='", "'<>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "DIV", "MUL", "SUM", "RES", "MENOR", 
                      "MENORIGUAL", "MAJOR", "MAJORIGUAL", "IGUAL", "DIFERENT", 
                      "NUM", "VAR", "WS" ]

    RULE_root = 0
    RULE_statements = 1
    RULE_statement = 2
    RULE_cosIf = 3
    RULE_cosWhile = 4
    RULE_expr = 5

    ruleNames =  [ "root", "statements", "statement", "cosIf", "cosWhile", 
                   "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    DIV=9
    MUL=10
    SUM=11
    RES=12
    MENOR=13
    MENORIGUAL=14
    MAJOR=15
    MAJORIGUAL=16
    IGUAL=17
    DIFERENT=18
    NUM=19
    VAR=20
    WS=21

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

        def statements(self):
            return self.getTypedRuleContext(exprsParser.StatementsContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.statements()
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
        self.enterRule(localctx, 2, self.RULE_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1048604) != 0):
                self.state = 14
                self.statement()
                self.state = 19
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


    class ImprimirContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(exprsParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImprimir" ):
                return visitor.visitImprimir(self)
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



    def statement(self):

        localctx = exprsParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                localctx = exprsParser.AsignarContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.match(exprsParser.VAR)
                self.state = 21
                self.match(exprsParser.T__0)
                self.state = 22
                self.expr(0)
                pass
            elif token in [2]:
                localctx = exprsParser.ImprimirContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.match(exprsParser.T__1)
                self.state = 24
                self.expr(0)
                pass
            elif token in [3]:
                localctx = exprsParser.CondicionalContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 25
                self.match(exprsParser.T__2)
                self.state = 26
                self.expr(0)
                self.state = 27
                self.cosIf()
                pass
            elif token in [4]:
                localctx = exprsParser.CondwhileContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 29
                self.match(exprsParser.T__3)
                self.state = 30
                self.expr(0)
                self.state = 31
                self.cosWhile()
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

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprsParser.StatementContext)
            else:
                return self.getTypedRuleContext(exprsParser.StatementContext,i)


        def getRuleIndex(self):
            return exprsParser.RULE_cosIf

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCosIf" ):
                return visitor.visitCosIf(self)
            else:
                return visitor.visitChildren(self)




    def cosIf(self):

        localctx = exprsParser.CosIfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_cosIf)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(exprsParser.T__4)
            self.state = 37 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 36
                self.statement()
                self.state = 39 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1048604) != 0)):
                    break

            self.state = 41
            self.match(exprsParser.T__5)
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

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprsParser.StatementContext)
            else:
                return self.getTypedRuleContext(exprsParser.StatementContext,i)


        def getRuleIndex(self):
            return exprsParser.RULE_cosWhile

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCosWhile" ):
                return visitor.visitCosWhile(self)
            else:
                return visitor.visitChildren(self)




    def cosWhile(self):

        localctx = exprsParser.CosWhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_cosWhile)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(exprsParser.T__6)
            self.state = 45 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 44
                self.statement()
                self.state = 47 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1048604) != 0)):
                    break

            self.state = 49
            self.match(exprsParser.T__5)
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
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                localctx = exprsParser.NumeroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 52
                self.match(exprsParser.NUM)
                pass
            elif token in [20]:
                localctx = exprsParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 53
                self.match(exprsParser.VAR)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 70
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 68
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = exprsParser.OpAritContext(self, exprsParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 56
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 57
                        self.match(exprsParser.T__7)
                        self.state = 58
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = exprsParser.OpAritContext(self, exprsParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 59
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 60
                        _la = self._input.LA(1)
                        if not(_la==9 or _la==10):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 61
                        self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = exprsParser.OpAritContext(self, exprsParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 62
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 63
                        _la = self._input.LA(1)
                        if not(_la==11 or _la==12):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 64
                        self.expr(5)
                        pass

                    elif la_ == 4:
                        localctx = exprsParser.OpLogicContext(self, exprsParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 65
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 66
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 516096) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 67
                        self.expr(4)
                        pass

             
                self.state = 72
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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
        self._predicates[5] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         




