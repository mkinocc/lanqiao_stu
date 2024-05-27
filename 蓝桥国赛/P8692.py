from collections import Counter


# 返回字典中第一个值
def fun1(my_dict):
    first_value = 0
    for key in my_dict:
        first_value = my_dict[key]
        break
    return first_value


k = int(input())
s = input().strip()

# 判断是否可以分成k节
if len(s) % k != 0:
    print(-1)
else:
    # 每个子字符串的长度(列数)， 行数就是k
    n = len(s) // k

    # 如果能分成k节，每一个循环节内的字符因该都是相同的，比如第一个“abc” 第二个应该也是“abc”
    # 如果说我们要求的是操作次数，那么我们因该把对应位的字符都改成一致的
    # 比如说“abc” 和 “bbc” 就得把第1位全部改成相同的
    # 要想修改的次数最少的话， 就得统计同位置最多次数的字符，然后用组数减去不同次数的字符就是操作数

    ans = 0

    # 遍历每一列
    for i in range(n):
        char_count = Counter()
        # 统计每个子字符串在该列位置上的字符出现次数
        for j in range(i, len(s), n):
            char_count[s[j]] += 1

        # 找到该列中出现最多的字符的次数
        max_freq = max(char_count.values())
        # 计算需要修改的字符数
        changes_needed = k - max_freq
        ans += changes_needed

    print(ans)

