#素因数とその個数を二次元リストとして返す関数
def to_prime(N):
    prime_lst = []
    i = 2
    while i ** 2 <= N:
        pow_time = 0
        while N % i == 0:
            pow_time += 1
            N //= i
        if pow_time:
            prime_lst.append([i,pow_time])
        i += 1
    if N >= 2:
        prime_lst.append([N, 1])

    return prime_lst
