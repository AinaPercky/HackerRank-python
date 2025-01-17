import math
import os
import random
import re
import sys
def solve(s):
    tab=s.split(' ')
    new_tab=[]
    full_name=''
    for i in range(0,len(tab)):
        new_tab.append(list(tab[i]))
    for item in new_tab:
        for j in range(0,len(item)):
            if(item[j].isnumeric() and j==0):
                break
            if (item[j].isalpha()):
                item[j]=item[j].upper()
                break
    for item in new_tab:
        full_name+=str(''.join(item))+' '
    return full_name

if __name__ == '__main__':

    s = input()

    result = solve(s)

    print(result)