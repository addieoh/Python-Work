plaintext = 'cat 0'
n = 2

letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'

def caesar_cipher(plaintext, n):
    result = ''

    for j in plaintext.lower():
        i = 0
        if j in letters:
            try:
                i = (letters.index(j) + n) % 26
                result += letters[i]
            except ValueError:
                result += j
        elif j in numbers:
            try:
                i = (numbers.index(j) + n) % 10
                result += numbers[i]
            except ValueError:
                result += j
        else:
            result += j
    return result
