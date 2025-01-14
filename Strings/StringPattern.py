def trianglePattern(level,char,desc=True,space=" "):
    count=1
    i=0
    while(i<level-1):
        count=count+2
        i=i+1
    if (desc==True):
        countSpace=0
        for i in range (count,0,-2):
            print(space*countSpace+char*i+space*countSpace)
            countSpace+=1
    else:
        countSpace=(count//2)
        for i in range (1,count+1,2):
            print(space*countSpace+char*i+space*countSpace)
            countSpace-=1
trianglePattern(6,'*')