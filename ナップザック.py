#EDPC (D) ナップザック問題
N, W = map(int, input().split())

U = [0]
V = [0]
for _ in range(N):
    u, v = map(int, input().split())
    U.append(u)
    V.append(v)

#i番目までの商品を選ぶとき、重さがjのときの価値の最大値
dp = [[0] * (W+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(W+1):
        if U[i] <= j:
            #商品を選んだ方が良いか判定
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-U[i]]+V[i])
        else:
            dp[i][j] = dp[i-1][j]


print(dp[N][W])