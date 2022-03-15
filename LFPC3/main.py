import lexer

def main ():

    content = ""
    with open('program.txt', 'r') as file:
        content = file.read()
    lex = lexer.Lexer(content)
    tokens = lex.tokenize
    print(tokens)

main()