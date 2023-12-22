#鉄則A-06
N, Q = map(int, input().split())
#添え字の関係上[0]を付けておくと便利。
A = [0] + list(map(int, input().split()))
#名前はSを付ける。appendしない、サイズを確保して初期化しておく
S = [0] * (N+1)

for i in range(1,N+1):
    #今までの累積和に今回の増分(A[i])を足す
    S[i] = A[i] + S[i-1]

for _ in range(Q):
    l,r = map(int, input().split())
    #S[r]-S[l-1]が閉区間[l,r]での累積和
    print(S[r]-S[l-1])
    
N = int(input())
S = " " + input()

X = [0]
for i in range(1,N):
    if S[i] == '<':
        X.append(X[i-1]+1)
    if S[i] == '>':
        X.append(X[i-1]-1)

print(X)
from collections import defaultdict
cnt = defaultdict(int)
upper = 0
ans = 0
cnt[0] += 1
for i in range(1,N):
    now = X[i]
    pre = X[i-1]
    if now < pre:
        upper += cnt[pre]
    else:
        upper = max(0,upper-cnt[now])
    print(now, upper)
    cnt[now] += 1

print(ans)