import sys
import re

# scanner
def validate_lexemes():
    global sentence
    for lexeme in sentence:
        if (not valid_lexeme(lexeme)):
            return False
    return True

def valid_lexeme(lexeme):
    return re.match(r'^[1-9]\d*(\.\d+)?$', lexeme)

def getNextLexeme():
    global lexeme
    global lexeme_index
    global sentence
    global num_lexemes
    global error
    lexeme_index = lexeme_index + 1
    if (lexeme_index < num_lexemes):
        lexeme = sentence[lexeme_index]
    else:
        lexeme = " "

# parser
# <number_expr> ::= <integer> | <float>
# <integer> ::= [1-9] [0-9]*
# <float> ::= [1-9] [0-9]* . [0-9]+

def number_expr():
    global lexeme
    global lexeme_index
    global num_lexemes
    global error
    if not re.match(r'^[1-9]\d*$', lexeme):
        if not re.match(r'^[1-9]\d*\.\d+$', lexeme):
            error = True
        else:
            getNextLexeme()
    else:
        getNextLexeme()

# main program
while True:
    line = input('Enter number: ')
    sentence = line.split()
    num_lexemes = len(sentence)
    lexeme_index = -1
    error = False
    if validate_lexemes():
        getNextLexeme()
        number_expr()
        if error or lexeme_index < num_lexemes:
            print('"{}" is not a valid number.'.format(line))
        else:
            print('"{}" is a valid number.'.format(line))
    else:
        print('"{}" contains invalid lexemes and, thus, '
              'is not a valid number.'.format(line))
