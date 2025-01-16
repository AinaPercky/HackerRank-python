def string_pattern_door_mat(n, string ,space,inverted=False):
    lines=[]
    total=n*3
    mid=((n*3)-3)//2
    if(inverted==False):
        for i in range(0, n*3, 3):
            if(mid-i<3):
                break
            else:
                if(i==0):
                    line=space*(mid-i)+string+space*(mid-i)
                else:
                    line=space*(mid-i)+string*((total-((mid-i)*2))//3)+space*(mid-i)
                lines.append(line)
    else:
        for i in range(3, n*3, 3):
            if(mid-i<0):
                break
            else:
                if(mid-i==0):
                    line=space*i+string+space*i
                else:
                    line=space*i+string*((total-(i*2))//3)+space*i
            lines.append(line)
    return  '\n'.join(lines)
