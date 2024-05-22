list1=[]

for i in range(30):
    list1.append(i+1)


for j in range(28):
    good=int(input())
    list1.remove(good)

list1.sort()
print(list1[0])
print(list1[1])