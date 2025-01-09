if __name__ == '__main__':
    N = int(input())
    list = []
    for i in range(N):
        command=input().split()
        commanInstruction=command[0]
        if(command[0]=='insert'):
            list.insert(int(command[1]),int(command[2]))
    print(list)
