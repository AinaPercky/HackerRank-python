def split_and_join(line):
    lineTab=line.split()
    joinedLine=''
    for i in range(len(lineTab)):
        if(i==len(lineTab)-1):
            joinedLine=joinedLine+lineTab[i]
        else:
            joinedLine=joinedLine+lineTab[i]+'-'
    return joinedLine

if __name__ == '__main__':
    line = input()
    result=split_and_join(line)
    print(result)