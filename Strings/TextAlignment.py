n = int(input())
volume = n * n
string = 'H'
doubleString = string + string
fiveString = string * 5

def numberString(argstring, number):
    i = 0
    while i < (number - 1):
        argstring += argstring[0]
        i += 1
    return argstring

def mutate_string(string, position, character):
    string = list(string)
    string[position] = character
    string = ''.join(string)
    return string

for i in range(0, n * 2, 2):
    print(string.center(9, ' '))
    string += doubleString

for i in range(n + 1):
    print(fiveString.center(9, ' '), end="")
    print('           ', end="")
    print(fiveString.center(9, ' '))

for i in range((n + 1) // 2):
    print('  ', end="")
    print(string.center(25, 'H'))

for i in range(n + 1):
    print(fiveString.center(9, ' '), end="")
    print('           ', end="")
    print(fiveString.center(9, ' '))

print(numberString('H', 9).rjust(volume + 4, ' '))


