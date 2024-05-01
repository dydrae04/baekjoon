n=int(input())
result=0

for i in range(n):
    a=input().split()
    for j in a:
        j=int(j)
        result+=j
    print(result)
    result=0
