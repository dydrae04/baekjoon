# map 함수
# map(function, iterable)
# 첫 번쨰 매개변수로는 함수가 오고
# 두 번쨰 매개변수로는 반복 가능한 자료형(리스트, 튜플 등)이 온다
# split()함수도 정리

list1=[]
a=input()
b=a.split()
for i in b:
    i=int(i)
    list1.append(i)
a=list1[0]
b=list1[-1]
print(a-b)