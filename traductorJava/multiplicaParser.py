# Generated from multiplica.g4 by ANTLR 4.13.2
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
        4,1,14,69,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,5,
        0,14,8,0,10,0,12,0,17,9,0,1,0,4,0,20,8,0,11,0,12,0,21,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,5,2,35,8,2,10,2,12,2,38,9,2,1,
        3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,3,
        5,56,8,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,64,8,5,10,5,12,5,67,9,5,1,5,
        0,1,10,6,0,2,4,6,8,10,0,0,68,0,15,1,0,0,0,2,23,1,0,0,0,4,31,1,0,
        0,0,6,39,1,0,0,0,8,42,1,0,0,0,10,55,1,0,0,0,12,14,3,2,1,0,13,12,
        1,0,0,0,14,17,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,16,19,1,0,0,0,
        17,15,1,0,0,0,18,20,3,8,4,0,19,18,1,0,0,0,20,21,1,0,0,0,21,19,1,
        0,0,0,21,22,1,0,0,0,22,1,1,0,0,0,23,24,5,1,0,0,24,25,5,4,0,0,25,
        26,5,7,0,0,26,27,3,4,2,0,27,28,5,8,0,0,28,29,5,9,0,0,29,30,3,6,3,
        0,30,3,1,0,0,0,31,36,5,4,0,0,32,33,5,10,0,0,33,35,5,4,0,0,34,32,
        1,0,0,0,35,38,1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,5,1,0,0,0,38,
        36,1,0,0,0,39,40,5,2,0,0,40,41,3,10,5,0,41,7,1,0,0,0,42,43,5,3,0,
        0,43,44,5,7,0,0,44,45,5,4,0,0,45,46,5,7,0,0,46,47,5,5,0,0,47,48,
        5,10,0,0,48,49,5,5,0,0,49,50,5,8,0,0,50,51,5,8,0,0,51,9,1,0,0,0,
        52,53,6,5,-1,0,53,56,5,5,0,0,54,56,5,4,0,0,55,52,1,0,0,0,55,54,1,
        0,0,0,56,65,1,0,0,0,57,58,10,4,0,0,58,59,5,12,0,0,59,64,3,10,5,5,
        60,61,10,3,0,0,61,62,5,13,0,0,62,64,3,10,5,4,63,57,1,0,0,0,63,60,
        1,0,0,0,64,67,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,11,1,0,0,0,
        67,65,1,0,0,0,6,15,21,36,55,63,65
    ]

class multiplicaParser ( Parser ):

    grammarFileName = "multiplica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'def'", "'return'", "'print'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'('", "')'", "':'", "','", 
                     "'='", "'*'", "'-'", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "DEF", "RETURN", "PRINT", "ID", "NUMBER", 
                      "WS", "LPAREN", "RPAREN", "COLON", "COMMA", "EQ", 
                      "MULT", "MINUS", "NEWLINE" ]

    RULE_program = 0
    RULE_functionDef = 1
    RULE_params = 2
    RULE_body = 3
    RULE_main = 4
    RULE_expr = 5

    ruleNames =  [ "program", "functionDef", "params", "body", "main", "expr" ]

    EOF = Token.EOF
    DEF=1
    RETURN=2
    PRINT=3
    ID=4
    NUMBER=5
    WS=6
    LPAREN=7
    RPAREN=8
    COLON=9
    COMMA=10
    EQ=11
    MULT=12
    MINUS=13
    NEWLINE=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(multiplicaParser.FunctionDefContext)
            else:
                return self.getTypedRuleContext(multiplicaParser.FunctionDefContext,i)


        def main(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(multiplicaParser.MainContext)
            else:
                return self.getTypedRuleContext(multiplicaParser.MainContext,i)


        def getRuleIndex(self):
            return multiplicaParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = multiplicaParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 12
                self.functionDef()
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.main()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==3):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEF(self):
            return self.getToken(multiplicaParser.DEF, 0)

        def ID(self):
            return self.getToken(multiplicaParser.ID, 0)

        def LPAREN(self):
            return self.getToken(multiplicaParser.LPAREN, 0)

        def params(self):
            return self.getTypedRuleContext(multiplicaParser.ParamsContext,0)


        def RPAREN(self):
            return self.getToken(multiplicaParser.RPAREN, 0)

        def COLON(self):
            return self.getToken(multiplicaParser.COLON, 0)

        def body(self):
            return self.getTypedRuleContext(multiplicaParser.BodyContext,0)


        def getRuleIndex(self):
            return multiplicaParser.RULE_functionDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDef" ):
                listener.enterFunctionDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDef" ):
                listener.exitFunctionDef(self)




    def functionDef(self):

        localctx = multiplicaParser.FunctionDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_functionDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(multiplicaParser.DEF)
            self.state = 24
            self.match(multiplicaParser.ID)
            self.state = 25
            self.match(multiplicaParser.LPAREN)
            self.state = 26
            self.params()
            self.state = 27
            self.match(multiplicaParser.RPAREN)
            self.state = 28
            self.match(multiplicaParser.COLON)
            self.state = 29
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(multiplicaParser.ID)
            else:
                return self.getToken(multiplicaParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(multiplicaParser.COMMA)
            else:
                return self.getToken(multiplicaParser.COMMA, i)

        def getRuleIndex(self):
            return multiplicaParser.RULE_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)




    def params(self):

        localctx = multiplicaParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(multiplicaParser.ID)
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 32
                self.match(multiplicaParser.COMMA)
                self.state = 33
                self.match(multiplicaParser.ID)
                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(multiplicaParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(multiplicaParser.ExprContext,0)


        def getRuleIndex(self):
            return multiplicaParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)




    def body(self):

        localctx = multiplicaParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(multiplicaParser.RETURN)
            self.state = 40
            self.expr(0)
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

        def PRINT(self):
            return self.getToken(multiplicaParser.PRINT, 0)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(multiplicaParser.LPAREN)
            else:
                return self.getToken(multiplicaParser.LPAREN, i)

        def ID(self):
            return self.getToken(multiplicaParser.ID, 0)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(multiplicaParser.NUMBER)
            else:
                return self.getToken(multiplicaParser.NUMBER, i)

        def COMMA(self):
            return self.getToken(multiplicaParser.COMMA, 0)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(multiplicaParser.RPAREN)
            else:
                return self.getToken(multiplicaParser.RPAREN, i)

        def getRuleIndex(self):
            return multiplicaParser.RULE_main

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain" ):
                listener.enterMain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain" ):
                listener.exitMain(self)




    def main(self):

        localctx = multiplicaParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_main)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(multiplicaParser.PRINT)
            self.state = 43
            self.match(multiplicaParser.LPAREN)
            self.state = 44
            self.match(multiplicaParser.ID)
            self.state = 45
            self.match(multiplicaParser.LPAREN)
            self.state = 46
            self.match(multiplicaParser.NUMBER)
            self.state = 47
            self.match(multiplicaParser.COMMA)
            self.state = 48
            self.match(multiplicaParser.NUMBER)
            self.state = 49
            self.match(multiplicaParser.RPAREN)
            self.state = 50
            self.match(multiplicaParser.RPAREN)
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

        def NUMBER(self):
            return self.getToken(multiplicaParser.NUMBER, 0)

        def ID(self):
            return self.getToken(multiplicaParser.ID, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(multiplicaParser.ExprContext)
            else:
                return self.getTypedRuleContext(multiplicaParser.ExprContext,i)


        def MULT(self):
            return self.getToken(multiplicaParser.MULT, 0)

        def MINUS(self):
            return self.getToken(multiplicaParser.MINUS, 0)

        def getRuleIndex(self):
            return multiplicaParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = multiplicaParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.state = 53
                self.match(multiplicaParser.NUMBER)
                pass
            elif token in [4]:
                self.state = 54
                self.match(multiplicaParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 65
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 63
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = multiplicaParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 57
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 58
                        self.match(multiplicaParser.MULT)
                        self.state = 59
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = multiplicaParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 60
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 61
                        self.match(multiplicaParser.MINUS)
                        self.state = 62
                        self.expr(4)
                        pass

             
                self.state = 67
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

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
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         




