#アルファベットと数値の対応表
from collections import defaultdict
import string
D = defaultdict(int)
for char in string.ascii_lowercase:
    D[char] = ord(char) - ord("a") + 1

#print(D)

#入力
N, Q = map(int, input().split())
S = input()

#ハッシュ値を計算するための変数
Mod = 2147483647
H = [0] * (N+1)