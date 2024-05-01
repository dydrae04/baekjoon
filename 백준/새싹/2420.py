y=input().split()
y[0], y[-1]= int(y[0]), int(y[-1])
sum=abs(y[0]-y[-1])
print(sum)