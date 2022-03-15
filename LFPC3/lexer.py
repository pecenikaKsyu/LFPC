import re
import lexDict

class Lexer(object):

    def __init__(self, source_code):
        self.source_code = source_code

    @property
    def tokenize(self):
        # where all the tokens created by lexer will be stored
        tokens = []
        # Create a word list of the source code
        source_code = self.source_code.split()
        # track the index of the word we are in code
        source_index = 0
        # loop to generate tokens
        while source_index < len(source_code):
            word = source_code[source_index]
            if word in lexDict.reserved:
                tokens.append([lexDict.reserved.get(word,0), word])
            elif re.match("[a-z]", word) or re.match("[A-Z]", word):
                if word[len(word)-1] in lexDict.literals:
                    if word[len(word)-2] in lexDict.literals:
                        ind = 0
                        for i in range(len(word)-1):
                            if word[i] not in lexDict.literals:
                                ind += 1
                            else:
                                tokens.append(['IDENIFIER', word[0:ind]])
                                while ind < len(word):
                                    tokens.append([lexDict.literals.get(word[ind], 0), word[ind]])
                                    ind +=1
                                break
                    else:
                        tokens.append(['IDENTIFIER', word[0:len(word)-1]])
                        tokens.append([lexDict.literals.get(word[len(word)-1]), word[len(word)-1]])
                else:
                    tokens.append(['IDENTIFIER', word])
            elif re.match("[0-9]", word):
                if word[len(word)-1] in lexDict.literals:
                    if '.' in word:
                        tokens.append(['float', word[0:len(word) - 1]])
                        tokens.append([lexDict.literals.get(word[len(word) - 1], 0), word[len(word) - 1]])
                    else:
                        tokens.append(['INTEGER', word[0:len(word)-1]])
                        tokens.append([lexDict.literals.get(word[len(word) - 1], 0), word[len(word) - 1]])
                else:
                    if '.' in word:
                        tokens.append(['float', word])
                    else:
                        tokens.append(['INTEGER', word])
            elif word in lexDict.literals:
                tokens.append([lexDict.literals.get(word, 0), word])
            elif word[0] == '#':
                pass
            else:
                tokens.append(['UNKNOWN_TOKEN', word])

            source_index += 1
        return tokens
