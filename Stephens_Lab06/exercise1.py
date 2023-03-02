import sys


def validate_lexemes():
    global sentence
    for lexeme in sentence:
        if (not valid_lexeme(lexeme)):
            return False
    return True


def valid_lexeme(lexeme):
    return lexeme in ["1"]


def getNextLexeme():
    global lexeme
    global lexeme_index
    global sentence
    global num_lexemes
    lexeme_index = lexeme_index + 1
    if (lexeme_index < num_lexemes):
        lexeme = sentence[lexeme_index]
    else:
        lexeme = ""


def count_ones():
    global lexeme
    global counter
    if lexeme == "1":
        counter += 1
        getNextLexeme()
        count_ones()


def expr():
    global lexeme
    global error
    global counter
    if lexeme == "":
        return

    if lexeme == "1":
        count_ones()
        if lexeme != "":
            if lexeme == "+":
                getNextLexeme()
                count_ones()
                expr()
            else:
                error = True
        return

    error = True


# main program
while True:
    line = input('Enter expression: ')
    sentence = list(line)
    num_lexemes = len(sentence)
    lexeme_index = -1
    error = False
    counter = 0

    if line == "-1":
        break

    if validate_lexemes():
        getNextLexeme()
        expr()
        if lexeme == "" and not error:
            print("The number of 1's is:", counter)
        else:
            print("Error")
    else:
        print('"{}" contains invalid lexemes and, thus, '
              'is not a sentence.'.format(line))
