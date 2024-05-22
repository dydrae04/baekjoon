import sys
N, X = map(int, sys.stdin.readline().split())
nums=list(map(int, input().split()))


for ii in nums:
    if ii<X:
        print(ii)

