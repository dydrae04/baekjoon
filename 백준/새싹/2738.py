#와 미친 개빡대가리 행열 반대로 ㅏㅣㅁㅇ누;히ㅏ뭏;ㅣ암ㄴ

n_m=input().split()

A_hang=[]
B_hang=[]

answer=[]

n=int(n_m[0])#행
m=int(n_m[-1])#열

for i in range(n):
    A=map(int, input().split())
    for ii in A:
        A_hang.append(ii)

for j in range(n):
    B=map(int, input().split())
    for jj in B:
        B_hang.append(jj)

for h in range(n*m):
    answer.append(A_hang[h]+B_hang[h])


for k in range(m*n):
    if (k+1)%m==0:
        print(answer[k])
    else:
        print(answer[k], end=" ")
