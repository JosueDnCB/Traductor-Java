# Generated from multiplica.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .multiplicaParser import multiplicaParser
else:
    from multiplicaParser import multiplicaParser

# This class defines a complete listener for a parse tree produced by multiplicaParser.
class multiplicaListener(ParseTreeListener):

    # Enter a parse tree produced by multiplicaParser#program.
    def enterProgram(self, ctx:multiplicaParser.ProgramContext):
        pass

    # Exit a parse tree produced by multiplicaParser#program.
    def exitProgram(self, ctx:multiplicaParser.ProgramContext):
        pass


    # Enter a parse tree produced by multiplicaParser#functionDef.
    def enterFunctionDef(self, ctx:multiplicaParser.FunctionDefContext):
        pass

    # Exit a parse tree produced by multiplicaParser#functionDef.
    def exitFunctionDef(self, ctx:multiplicaParser.FunctionDefContext):
        pass


    # Enter a parse tree produced by multiplicaParser#params.
    def enterParams(self, ctx:multiplicaParser.ParamsContext):
        pass

    # Exit a parse tree produced by multiplicaParser#params.
    def exitParams(self, ctx:multiplicaParser.ParamsContext):
        pass


    # Enter a parse tree produced by multiplicaParser#body.
    def enterBody(self, ctx:multiplicaParser.BodyContext):
        pass

    # Exit a parse tree produced by multiplicaParser#body.
    def exitBody(self, ctx:multiplicaParser.BodyContext):
        pass


    # Enter a parse tree produced by multiplicaParser#main.
    def enterMain(self, ctx:multiplicaParser.MainContext):
        pass

    # Exit a parse tree produced by multiplicaParser#main.
    def exitMain(self, ctx:multiplicaParser.MainContext):
        pass


    # Enter a parse tree produced by multiplicaParser#expr.
    def enterExpr(self, ctx:multiplicaParser.ExprContext):
        pass

    # Exit a parse tree produced by multiplicaParser#expr.
    def exitExpr(self, ctx:multiplicaParser.ExprContext):
        pass



del multiplicaParser