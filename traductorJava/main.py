from antlr4 import *
from multiplicaLexer import multiplicaLexer
from multiplicaParser import multiplicaParser
from TraduceToJava import JavaGeneratorListener
from antlr4.tree.Tree import ParseTreeWalker

def main():
    in_code = '/Users/josuedaniel/Documents/7 Semestre/Lenguajes y automatas 1/java2/traductorJava/muestra.txt'
    
    with open(in_code, 'r') as fileOpen:
        content = fileOpen.read()
        print("Contenido del archivo:")
        print(repr(content))  

    input_stream = InputStream(content)
    
    # Lexer y Parser
    lexer = multiplicaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = multiplicaParser(stream)
    
    for token in stream.tokens:
     print(f"Token: {token.text}, Tipo: {lexer.symbolicNames[token.type]}")

    # Parsear el programa
    tree = parser.program()
    
    # Listener para generar el código Java
    listener = JavaGeneratorListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    print(tree.toStringTree(recog=parser))

    # Guardar el archivo Java generado
    with open("Main.java", "w") as java_file:
        java_file.write(listener.result_code)

if __name__ == "__main__":
    main()
