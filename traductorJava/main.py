from antlr4 import *
import sys
from antlr4 import FileStream, CommonTokenStream
from multiplicaLexer import multiplicaLexer
from multiplicaParser import multiplicaParser
from TraduceToJava import JavaGeneratorListener
from antlr4.tree.Tree import ParseTreeWalker

def main(input_file):
    # Leer el archivo de entrada
    input_stream = FileStream(input_file)
    
    # Lexer y Parser
    lexer = multiplicaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = multiplicaParser(stream)
    
    # Regla inicial: parsear el programa
    tree = parser.program()  # La regla inicial es 'program'
    
    # Listener para generar el código Java
    listener = JavaGeneratorListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)  # Camina el árbol de parseo con el listener
    
    # Guardar el archivo Java generado
    with open("muestra.java", "w") as java_file:
        java_file.write(listener.result_code)

if __name__ == "__main__":
    # Leer el archivo de entrada desde los argumentos de la línea de comandos
    input_file = sys.argv[1]
    main(input_file)
