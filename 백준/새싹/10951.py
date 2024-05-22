sum=0

while True:
    try:
        num=input().split()
        for i in num:
            i=int(i)
            sum+=i
        if sum==0:
            break
        else:
            print(sum)
            sum=0
    except:
        break

