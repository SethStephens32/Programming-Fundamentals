import sys

# scanner
def validate_lexemes():
    global sentence
    for lexeme in sentence:
        if not valid_lexeme(lexeme):
            return False
    return True

def valid_lexeme(lexeme):
    return is_digitL(lexeme) or is_digit(lexeme)

def is_digitL(lexeme):
    if not lexeme:
        return False
    if lexeme[0] == "0" and len(lexeme) > 1:
        return False
    for c in lexeme:
        if c < "0" or c > "9":
            return False
    return True

def is_digit(lexeme):
    if not lexeme or "." not in lexeme:
        return False
    if lexeme[0] == "0" and lexeme[1] != ".":
        return False
    digitL_part, decimal_part = lexeme.split(".")
    if not digitL_part and not decimal_part:
        return False
    if not is_digitL(digitL_part) or not is_digitL(decimal_part):
        return False
    return True

def getNextLexeme():
    global lexeme
    global lexeme_index
    global sentence
    global num_lexemes
    global error
    lexeme_index = lexeme_index + 1
    if lexeme_index < num_lexemes:
        lexeme = sentence[lexeme_index]
    else:
        lexeme = " "

# parser
# <number_expr> ::= <digitL> | <digit>
# <digitL> ::= [0-9]*
# <digit> ::= [1-9] 

def number_expr():
    global lexeme
    global lexeme_index
    global num_lexemes
    global error
    if not is_digitL(lexeme):
        if not is_digit(lexeme):
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
