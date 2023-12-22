#ABC204 C
from collections import deque
n, m = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)


visit = [[-1] * n for _ in range(n)]
ans = 0
for i in range(n):
    que = deque()
    visit[i][i] = 1
    que.append(i)
    while que:
        cur = que.popleft()
        for nex in G[cur]:
            if visit[i][nex] == -1:
                visit[i][nex] = 1
                que.append(nex)
    for j in range(n):
        if visit[i][j] == 1:
            ans += 1

print(ans)