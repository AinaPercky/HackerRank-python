from StingPatternDoorMat import string_pattern_door_mat
n = input()
tab=n.split()
N=int(tab[0])
M=int(tab[1])
print(string_pattern_door_mat(N, '.|.', '-'))
print('WELCOME'.center(M, '-'))
print(string_pattern_door_mat(N, '.|.', '-',True))