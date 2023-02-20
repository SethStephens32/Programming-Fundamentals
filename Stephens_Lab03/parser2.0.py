import sys

# Function to check if each lexeme (digit) is valid
def validate_lexemes():
    global sentence
    for lexeme in sentence:
        if not valid_lexeme(lexeme):
            return False
    return True

# Function to check if a lexeme (digit) is valid
def valid_lexeme(lexeme):
    return lexeme in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Function to get the next lexeme (digit)
def getNextLexeme():
    global lexeme
    global lexeme_index
    global sentence
    global num_lexemes
    global error

    # Increment the lexeme index
    lexeme_index = lexeme_index + 1

    # If there are more lexemes, get the next one
    if lexeme_index < num_lexemes:
        lexeme = sentence[lexeme_index]
    else:
        # Otherwise, set the lexeme to a space
        lexeme = " "

# Function to parse a number expression
def number_expr():
    global lexeme
    global lexeme_index
    global num_lexemes
    global error

    # List of valid lexemes for digitL
    digitL = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # List of valid lexemes for digit
    digit = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    # Check if the first lexeme is 0, which is not allowed unless it's the only lexeme
    if lexeme == '0' and lexeme_index == 0:
        error = True
        return

    # Get the next lexeme
    getNextLexeme()

    # If the current lexeme is a valid digitL or digit, recursively call the function to check the next lexeme
    if lexeme in digitL or lexeme in digit:
        number_expr()
    # If the current lexeme is a space or the end of the sentence, the expression is valid
    elif lexeme == ' ' or lexeme == 0:
        return
    # Otherwise, the expression is invalid
    else:
        error = True
        return

# Loop to get user input and parse number expressions
while True:
    # Get user input and add a space between each digit
    sentence = input("Enter a number:")
    sentence = sentence.replace(" ", "")

    # Set up global variables
    lexeme = sentence[0]
    lexeme_index = 0
    num_lexemes = len(sentence)
    error = False

    # Check if the lexemes are valid and parse the number expression
    if validate_lexemes():
        number_expr()

    # Print the result
    if error:
        print("Invalid Sentence")
    else:
        print("Valid Sentence")
