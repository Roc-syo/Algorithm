#計算量O(logN)で約数のリストを返す

def make_divisors(n):
    #lower: 小さい方の約数, upper: 大きい方の約数
    lower_divisors, upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % 1 == 0:
            lower_divisors.append(i)
            if i != n//i:
                upper_divisors.append(n//i)
        i += 1
    
    return lower_divisors + upper_divisors[::-1]
