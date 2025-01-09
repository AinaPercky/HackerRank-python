def validateNum(string):
    num=False
    for i in string:
        if i.isalnum():
            num=True
            return num
    return num

def validateAlpha(string):
    alpha=False
    for i in string:
        if i.isalpha():
            alpha=True
            return alpha
    return alpha

def validateDigit(string):
    digit=False
    for i in string:
        if i.isdigit():
            digit=True
            return digit
    return digit

def validatelower(string):
    lower=False
    for i in string:
        if i.islower():
            lower=True
            return lower
    return lower

def validateupper(string):
    upper=False
    for i in string:
        if i.isupper():
            upper=True
            return upper
    return upper

if __name__ == '__main__':
    s = input()
    print(validateNum(s))
    print(validateAlpha(s))
    print(validateDigit(s))
    print(validatelower(s))
    print(validateupper(s))
