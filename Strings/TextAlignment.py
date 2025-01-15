

from StringPattern import trianglePattern
n = int(input())
volume = n * n
string = 'H'
doubleString = string + string
fiveString = string * 5

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
# print('           ', end="")
print(trianglePattern(5,'H',True," ",20))
# print((trianglePattern(5,'H')).rjust(70, ' '))

# print(trianglePattern(5,'H'))


