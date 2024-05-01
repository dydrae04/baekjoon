sum=0
a=0

while a<5:
    n=input().split()
    for i in n:
        i=int(i)
        sum+=i
    print(sum)
    sum=0
    a+=1

    