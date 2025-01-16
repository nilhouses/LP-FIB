# Generated from exprs.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,7,37,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,4,5,27,8,5,11,
        5,12,5,28,1,6,4,6,32,8,6,11,6,12,6,33,1,6,1,6,0,0,7,1,1,3,2,5,3,
        7,4,9,5,11,6,13,7,1,0,2,1,0,48,57,3,0,9,10,13,13,32,32,38,0,1,1,
        0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,
        0,0,13,1,0,0,0,1,15,1,0,0,0,3,17,1,0,0,0,5,19,1,0,0,0,7,21,1,0,0,
        0,9,23,1,0,0,0,11,26,1,0,0,0,13,31,1,0,0,0,15,16,5,43,0,0,16,2,1,
        0,0,0,17,18,5,45,0,0,18,4,1,0,0,0,19,20,5,42,0,0,20,6,1,0,0,0,21,
        22,5,47,0,0,22,8,1,0,0,0,23,24,5,94,0,0,24,10,1,0,0,0,25,27,7,0,
        0,0,26,25,1,0,0,0,27,28,1,0,0,0,28,26,1,0,0,0,28,29,1,0,0,0,29,12,
        1,0,0,0,30,32,7,1,0,0,31,30,1,0,0,0,32,33,1,0,0,0,33,31,1,0,0,0,
        33,34,1,0,0,0,34,35,1,0,0,0,35,36,6,6,0,0,36,14,1,0,0,0,3,0,28,33,
        1,6,0,0
    ]

class exprsLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    NUM = 6
    WS = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'^'" ]

    symbolicNames = [ "<INVALID>",
            "NUM", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "NUM", "WS" ]

    grammarFileName = "exprs.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


