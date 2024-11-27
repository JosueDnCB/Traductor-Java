from multiplicaListener import multiplicaListener
from multiplicaParser import *

class JavaGeneratorListener(multiplicaListener):
    def __init__(self):
        self.result_code = ""
        self.functions_code = []  # Inicializar lista para funciones

    # Enter a parse tree produced by multiplicaParser#program.
    def enterProgram(self, ctx:multiplicaParser.ProgramContext):
        self.result_code = "public class Main {\n"
        self.result_code += "    public static void main(String[] args) {\n"

    # Exit a parse tree produced by multiplicaParser#program.
    def exitProgram(self, ctx:multiplicaParser.ProgramContext):
        self.result_code += "    }\n"  # Cerrar el main
        # Agregar todas las funciones después del main
        for function in self.functions_code:
            self.result_code += function
        self.result_code += "}\n"  # Cerrar la clase

    # Enter a parse tree produced by multiplicaParser#functionDef.
    def enterFunctionDef(self, ctx:multiplicaParser.FunctionDefContext):
        func_name = ctx.ID().getText()
        self.current_function = f"    public static int {func_name}(int A, int B) {{\n"

    # Exit a parse tree produced by multiplicaParser#functionDef.
    def exitFunctionDef(self, ctx:multiplicaParser.FunctionDefContext):
        self.current_function += "        return A * B - A;\n"
        self.current_function += "    }\n"
        # Se Agrega la función completa a la lista
        self.functions_code.append(self.current_function)

    # Enter a parse tree produced by multiplicaParser#main.
    def enterMain(self, ctx:multiplicaParser.MainContext):
        self.result_code += "        int result = multiplica(5, 6);\n"
        self.result_code += "        System.out.println(result);\n"

    def exitMain(self, ctx:multiplicaParser.MainContext):
        pass
