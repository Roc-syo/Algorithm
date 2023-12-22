#鉄則A58
#問題によってsegfunc, update, Arrayを変える
class SegTree:
    def __init__(self, Array, init, segfunc):
        #初期元(演算に合わせて入力)
        self.init = init
        #セグメント木の高さ → 入力配列サイズのビット長+1
        self.height = len(Array).bit_length()+1
        #演算の種類(和・積・論理和など)
        self.segfunc = segfunc
        #最下段の左端のインデックス
        self.num = 2**(self.height-1)
        #木
        self.Tree = [init] * pow(2, self.height)
        #最下段をセット
        for i in range(len(Array)):
            self.Tree[self.num+i] = Array[i]
        #セグメント木を下段から構築
        for i in range(self.num-1, 0, -1):
            self.Tree[i] = self.segfunc(self.Tree[i*2], self.Tree[i*2+1])
    #値の更新
    def update(self, k, x):
        pos = self.num + k
        #最下段の更新
        self.Tree[pos] = x
        #下段から根まで更新していく
        while pos > 1:
            #親から見て左だったら  
            if pos % 2 == 0:
                self.Tree[pos//2] = self.segfunc(self.Tree[pos], self.Tree[pos+1])
            #右だったら
            else:
                self.Tree[pos//2] = self.segfunc(self.Tree[pos-1], self.Tree[pos])
            #今更新した位置に進める
            pos //= 2
    #(l,r 探索区間 l_now=0(左端),r_now=2**(st.height-1)-1(右端),now)
    def query(self, l, r, l_now, r_now, now=1):
        #探索範囲外のとき、適当な値を返す
        if l_now > r or r_now < l:
            return self.init
        #探索範囲に完全に収まっている場合、そのノードの値を返す
        if l <= l_now and r_now <= r:
            return self.Tree[now]
        #探索範囲に一部収まっている場合、左右の子を調べる
        else:
            mid = (l_now+r_now) // 2
            L_res = self.query(l, r, l_now, mid, now*2)
            R_res = self.query(l, r, mid+1, r_now, now*2+1)
            return self.segfunc(L_res, R_res)
        
        
        
    
def segfunc(a,b):
    return a+b

N, Q = map(int, input().split())
Array = [0] * N
st = SegTree(Array, -1, segfunc)

for _ in range(Q):
    que = list(map(int, input().split()))
    if que[0] == 1:
        st.update(que[1]-1,que[2])
    else:
        print(st.query(que[1]-1,que[2]-2,0,2**(st.height-1)-1))

print(st.Tree)