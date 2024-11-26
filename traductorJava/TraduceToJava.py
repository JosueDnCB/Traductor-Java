from multiplicaListener import multiplicaListener

class JavaGeneratorListener(multiplicaListener):
    def __init__(self):
        self.result_code = ""
    
    def enterFunctionDef(self, ctx):
        # Genera la firma de la función en Java
        func_name = ctx.ID().getText()
        params = ", ".join([param.getText() for param in ctx.params().ID()])
        self.result_code += f"public static int {func_name}({params}) {{\n"
    
    def exitFunctionDef(self, ctx):
        # Salida de la función
        self.result_code += "}\n"
    
    def enterReturn(self, ctx):
        # Convierte la expresión de retorno a Java
        expr = ctx.expr().getText()
        self.result_code += f"    return {expr};\n"
    
    def enterMain(self, ctx):
        # Entrada para el método main
        self.result_code += "public class Main {\n"
        self.result_code += "    public static void main(String[] args) {\n"
    
    def exitMain(self, ctx):
        # Salida para el método main
        self.result_code += "        int result = multiplica(5, 6);\n"
        self.result_code += "        System.out.println(result);\n"
        self.result_code += "    }\n"
        self.result_code += "}\n"
