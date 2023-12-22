class UnionFind:
    #UnionFindインスタンスの初期化(n: ノード数)
    def __init__(self, n):
        self.n = n
        #-x: グループのサイズ(自身が根) k(正):根がk
        self.parent_size = [-1]*n
    #merge: ノードa, ノードbを辺で結ぶ
    def merge(self, a, b):
        x, y = self.leader(a), self.leader(b)
        if x == y: 
            return
        #根同士のサイズを比較
        if abs(self.parent_size[x]) < abs(self.parent_size[y]):
            x, y = y, x  
        #サイズが大きい方に小さい方を吸収させる
        self.parent_size[x] += self.parent_size[y]
        #吸収された方の根を更新する
        self.parent_size[y] = x
        return
    #same: 同じグループか判定
    def same(self, a, b):
        return self.leader(a) == self.leader(b)
    
    #leader: aの根を示す
    def leader(self, a):
        #aが根ならaを返す
        if self.parent_size[a]<0:
            return a
        #aが根で無いのなら、根に向かってたどる & aの根を更新する
        self.parent_size[a] = self.leader(self.parent_size[a])
        return self.parent_size[a]
    
    def size(self,a):
        return abs(self.parent_size[self.leader(a)])

    def groups(self):
        result = [[] for _ in range(self.n)]
        for i in range(self.n):
            result[self.leader(i)].append(i)
        return [r for r in result if r != []]
    