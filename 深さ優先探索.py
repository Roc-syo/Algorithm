#鉄則A62 グラフが連結かどうか調べる問題
import sys
sys.setrecursionlimit(10**8)

N, M = map(int, input().split())

G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

visited = [False for _ in range(N)]

def dfs(cur,G):
    visited[cur] = True

    for nex in G[cur]:
        if visited[nex] == False:
            dfs(nex,G)
    #終了
    return True

dfs(0,G)

flag = True
for u in visited:
    if u != True:
        flag = False

print("The graph is ",end="")
print("connected." if flag else "not connected.")