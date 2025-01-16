def print_formatted(number):
    lines=[]
    space=" "
    for i in range (1,number+1):
        string=''
        for j in range (1,5):
            if (j==1):
                print((str(i)),end=' ')
            elif(j==2):
                print(str(oct(i)).replace('0o',''),end=' ')
            elif(j==3):
                print(str(hex(i)).replace('0x',''),end=' ')
            else:
                print(str(bin(i)).replace('0b',''),end=' ')
        lines.append(string)
        print(' ')
    return '\n'.join(lines)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
