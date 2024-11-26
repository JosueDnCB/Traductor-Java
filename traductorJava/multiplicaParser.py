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
        4,1,14,64,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,4,0,15,8,0,11,0,12,0,16,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,
        2,1,2,5,2,30,8,2,10,2,12,2,33,9,2,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,3,5,51,8,5,1,5,1,5,1,5,1,5,1,5,
        1,5,5,5,59,8,5,10,5,12,5,62,9,5,1,5,0,1,10,6,0,2,4,6,8,10,0,0,63,
        0,14,1,0,0,0,2,18,1,0,0,0,4,26,1,0,0,0,6,34,1,0,0,0,8,37,1,0,0,0,
        10,50,1,0,0,0,12,15,3,2,1,0,13,15,3,8,4,0,14,12,1,0,0,0,14,13,1,
        0,0,0,15,16,1,0,0,0,16,14,1,0,0,0,16,17,1,0,0,0,17,1,1,0,0,0,18,
        19,5,8,0,0,19,20,5,2,0,0,20,21,5,4,0,0,21,22,3,4,2,0,22,23,5,5,0,
        0,23,24,5,6,0,0,24,25,3,6,3,0,25,3,1,0,0,0,26,31,5,2,0,0,27,28,5,
        7,0,0,28,30,5,2,0,0,29,27,1,0,0,0,30,33,1,0,0,0,31,29,1,0,0,0,31,
        32,1,0,0,0,32,5,1,0,0,0,33,31,1,0,0,0,34,35,5,9,0,0,35,36,3,10,5,
        0,36,7,1,0,0,0,37,38,5,13,0,0,38,39,5,4,0,0,39,40,5,2,0,0,40,41,
        5,4,0,0,41,42,5,1,0,0,42,43,5,7,0,0,43,44,5,1,0,0,44,45,5,5,0,0,
        45,46,5,5,0,0,46,9,1,0,0,0,47,48,6,5,-1,0,48,51,5,1,0,0,49,51,5,
        2,0,0,50,47,1,0,0,0,50,49,1,0,0,0,51,60,1,0,0,0,52,53,10,4,0,0,53,
        54,5,11,0,0,54,59,3,10,5,5,55,56,10,3,0,0,56,57,5,12,0,0,57,59,3,
        10,5,4,58,52,1,0,0,0,58,55,1,0,0,0,59,62,1,0,0,0,60,58,1,0,0,0,60,
        61,1,0,0,0,61,11,1,0,0,0,62,60,1,0,0,0,6,14,16,31,50,58,60
    ]

class multiplicaParser ( Parser ):

    grammarFileName = "multiplica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "':'", "','", "'Def'", "'Return'", "'='", 
                     "'*'", "'-'", "'print'", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "NUMBER", "ID", "WS", "LPAREN", "RPAREN", 
                      "COLON", "COMMA", "DEF", "RETURN", "EQ", "MULT", "MINUS", 
                      "PRINT", "NEWLINE" ]

    RULE_program = 0
    RULE_functionDef = 1
    RULE_params = 2
    RULE_body = 3
    RULE_main = 4
    RULE_expr = 5

    ruleNames =  [ "program", "functionDef", "params", "body", "main", "expr" ]

    EOF = Token.EOF
    NUMBER=1
    ID=2
    WS=3
    LPAREN=4
    RPAREN=5
    COLON=6
    COMMA=7
    DEF=8
    RETURN=9
    EQ=10
    MULT=11
    MINUS=12
    PRINT=13
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
            self.state = 14 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [8]:
                    self.state = 12
                    self.functionDef()
                    pass
                elif token in [13]:
                    self.state = 13
                    self.main()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 16 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==8 or _la==13):
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
            self.state = 18
            self.match(multiplicaParser.DEF)
            self.state = 19
            self.match(multiplicaParser.ID)
            self.state = 20
            self.match(multiplicaParser.LPAREN)
            self.state = 21
            self.params()
            self.state = 22
            self.match(multiplicaParser.RPAREN)
            self.state = 23
            self.match(multiplicaParser.COLON)
            self.state = 24
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
            self.state = 26
            self.match(multiplicaParser.ID)
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 27
                self.match(multiplicaParser.COMMA)
                self.state = 28
                self.match(multiplicaParser.ID)
                self.state = 33
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
            self.state = 34
            self.match(multiplicaParser.RETURN)
            self.state = 35
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
            self.state = 37
            self.match(multiplicaParser.PRINT)
            self.state = 38
            self.match(multiplicaParser.LPAREN)
            self.state = 39
            self.match(multiplicaParser.ID)
            self.state = 40
            self.match(multiplicaParser.LPAREN)
            self.state = 41
            self.match(multiplicaParser.NUMBER)
            self.state = 42
            self.match(multiplicaParser.COMMA)
            self.state = 43
            self.match(multiplicaParser.NUMBER)
            self.state = 44
            self.match(multiplicaParser.RPAREN)
            self.state = 45
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
            self.state = 50
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.state = 48
                self.match(multiplicaParser.NUMBER)
                pass
            elif token in [2]:
                self.state = 49
                self.match(multiplicaParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 60
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 58
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = multiplicaParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 52
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 53
                        self.match(multiplicaParser.MULT)
                        self.state = 54
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = multiplicaParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 55
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 56
                        self.match(multiplicaParser.MINUS)
                        self.state = 57
                        self.expr(4)
                        pass

             
                self.state = 62
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
         




