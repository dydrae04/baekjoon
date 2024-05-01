Tof=True
sum=0

while Tof:
    a=input().split()
    if a==["0", "0"]:
        Tof=False
    else:
        for i in a:
            i=int(i)
            sum+=i
        print(sum)
    sum=0
    
    
