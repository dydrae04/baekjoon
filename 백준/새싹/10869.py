a=input().split()
list1=[]
for i in a:
    i=int(i)
    list1.append(i)
print(list1[0]+list1[-1])
print(list1[0]-list1[-1])
print(list1[0]*list1[-1])
print(int(list1[0]/list1[-1]))
print(list1[0]%list1[-1])