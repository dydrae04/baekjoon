n=int(input())
nums=input().split()
v=input()

list1=[]
much=0

for i in nums:
    list1.append(i)

for j in list1:
    if j==v:
        much+=1

print(much)