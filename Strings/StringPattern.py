def trianglePattern(level,char,desc=True,space=" ",spaceBefore=0):
    result=''
    count=1
    i=0
    while(i<level-1):
        count=count+2
        i=i+1
    if (desc==True):
        countSpace=0
        for i in range (count,0,-2):
            result=result+space*spaceBefore+space*countSpace+char*i+space*countSpace
            result=result+'\n'
            # print(space*countSpace+char*i+space*countSpace)
            countSpace+=1
    else:
        countSpace=(count//2)
        for i in range (1,count+1,2):
            result=result+space*spaceBefore+space*countSpace+char*i+space*countSpace
            result=result+'\n'
            print(space*countSpace+char*i+space*countSpace)
            countSpace-=1
    return result

# print(trianglePattern(5,'*',True," ",10))
