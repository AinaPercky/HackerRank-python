from StringPattern import trianglePattern
n = int(input())
volume = n * n
string = 'H'
repeat_string = string * n

print(trianglePattern(n,string,False))

for i in range(n + 1):
    print(repeat_string.center(n*2-1, ' '), end="")
    print(' '*(n*2+1), end="")
    print(repeat_string.center(n*2-1, ' '))

for i in range((n + 1) // 2):
    print(' '*(((n*2-1)-n)//2), end="")
    print(string.center(n*5, string))

for i in range(n + 1):
    print(repeat_string.center(n*2-1, ' '), end="")
    print(' '*(n*2+1), end="")
    print(repeat_string.center(n*2-1, ' '))

print(trianglePattern(n,string,True," ",n*4))




