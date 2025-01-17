def entier_en_alphabet(entier):
    if 1 <= entier <= 26: 
        return chr(ord('a') + entier - 1) 
    else:
        return None 
def enlever_premier_et_dernier(chaine):
    if len(chaine) > 1: 
        return chaine[1:-1]
    return "" 

def print_rangoli(size):
    tab_lines = []
    alpabet_tab= []
    for i in range(0,size):
        alpabet_tab.append(entier_en_alphabet(size - i))
    for i in range(0,size+1):
        lines=''
        if (i==0):
            continue
        for j in range(0,i):
            if (j==0):
                lines+='-'+alpabet_tab[j]+'-'
            else:
                lines+=alpabet_tab[j]+'-'
        for k in range(i-1,0,-1):
            lines+=alpabet_tab[k-1]+'-'   
        tab_lines.append(lines)
    tab_lines[size-1]=enlever_premier_et_dernier(tab_lines[size-1])
    tab_lines_reverted = list(reversed(tab_lines)) 
    for i in tab_lines:
        print(i.center((size*4-3),'-'))
    for j in range(1,size):
        print(tab_lines_reverted[j].center((size*4-3),'-'))



if __name__ == '__main__':
    n = int(input())
    (print_rangoli(n))

