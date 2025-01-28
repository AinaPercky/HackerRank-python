n = int(input())
s = set(map(int, input().split()))
command_number=int(input())
for i in range (command_number):
    command=input().split(' ')
    if(command[0]=='pop'):
        s.pop()
    elif(command[0]=='remove'):
        s.remove(int(command[1]))
    elif(command[0]=='discard'):
        s.discard(int(command[1]))
    else:
        pass
for s_item in s:
    print(s_item)