def fun_a(s):
    # 定义一个数组dp[0~4]分别代表：“2”、“20”、“202”、“2023”的个数
    dp = [0] * 4

    for char in s:
        if char == '2':
            # 当是字符2的时候，2可以单独做一个字符串
            dp[0] += 1
            # 也可以跟在20后面，更新成202字符串
            dp[2] += dp[1]
        elif char == '0':
            # 当是字符0的时候，可以跟在2后面构成“20”
            dp[1] += dp[0]
        elif char == '3':
            # 当是字符3的时候，可以跟在202后面构成“2023”
            dp[3] += dp[2]

    return dp[3]


# 欧啦筛法，筛选出2～n所有的质数
def euler_sieve(n):
    is_prime = [True] * (n + 1)
    primes = []

    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return primes

def fun_b():
    # 因为sqrt（23333333333333）约等于 4830459
    # 所以筛选5 * 10 ** 6
    primes = euler_sieve(4830459)
    cnt = 0
    for i in range(len(primes)):
        p2 = (primes[i] * primes[i])
        # 如果p的四次方都爆了，那么p*p*q*q更要爆
        # 解释上面那句话，应该刚才筛完质数，p是小于q的
        if p2 * p2 > 23333333333333:
            break
        for j in range(i + 1, len(primes)):
            q2 = (primes[j] * primes[j])
            if p2 * q2 < 2333:
                continue
            if p2 * q2 > 23333333333333:
                break
            cnt += 1
    return cnt

if __name__ == '__main__':
    # 构造字符串
    a = str(input()).upper()
    mystr = ""
    for i in range(1, 2024):
        mystr += str(i)
    if a == "A":
        r = fun_a(mystr)
        print(str(r))
    if a == "B":
        p = fun_b()
        print(str(p))


