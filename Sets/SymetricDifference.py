a=input()
m = set(map(int, input().split()))  
b = input()
n = set(map(int, input().split()))  
symetric_difference=m.symmetric_difference(n)
symetric_difference=sorted(symetric_difference)
for symetric_difference_item in symetric_difference:
    print(symetric_difference_item)

