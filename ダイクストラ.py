#鉄則 A64 Shortest Path2
#ダイクストラ法
import heapq
#入力
N, M = map(int, input().split())
Graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    Graph[a].append([b,c])
    Graph[b].append([a,c])

kakutei = [False] * N
dist = [10 ** 15] * N

q = [[0,0]]
heapq.heapify(q)

while q:
    #最小コストのノードが取り出される
    cur = heapq.heappop(q)
    cost, pos = cur[0], cur[1]
    
    #確定した点が更新されないように
    if kakutei[pos] == True:
        continue
    
    kakutei[pos] = True
    dist[pos] = cost
    
    for nex in Graph[pos]:
        npos = nex[0]
        ncost = cost + nex[1]
        if dist[npos] > ncost:
            heapq.heappush(q, [ncost, npos])

for d in dist:
    print(d if d != 10**15 else -1)