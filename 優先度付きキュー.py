import heapq

A = [3,5,1,2,0]
#heapの構築(計算量はO(N))
heapq.heapify(A)


print(A)
#>>> [0, 2, 1, 3, 5]

#heappopで最小値を取り出す(最小値はヒープから消失する)

a = heapq.heappop(A)
print(a)
#>>> 0

#heappushで値を挿入
heapq.heappush(A, 18)
print(A)
#>>> [1, 2, 5, 3, 18]



