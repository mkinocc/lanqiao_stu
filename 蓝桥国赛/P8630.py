from collections import Counter

# 知道了每段固定长度也就是8长度后，比较是否满足密码的计数，满足就说明能找到一次
s = input().strip()
n = int(input().strip())
l = [input().strip() for _ in range(n)]

# 定义密码计数器字典，设置为列表包含
l_cou = list(Counter(char) for char in l)

ans = 0

# 初始化一个字典计数器，范围为0到7,测试s前8个字符记数
window_count = Counter(s[:8])


# print(window_count)

# 定义一个辅助函数来比较两个计数器
def counters_equal(c1, c2):
    return c1 == c2


for i in range(0, len(s) - 8 + 1):
    # 因为窗口长度是确定的 也就是当下标在len(s) - 8的时候其实已经包含到s的末尾了

    # 设置每次的起始位置和结束位置
    start_in = i
    end_in = i + 8 - 1
    # 记录当前比较后的字典数据
    curr_window = Counter(s[start_in:end_in + 1])

    # 遍历检查窗口是否满足条件(同时检查所有的密码了)
    for k in l_cou:
        if counters_equal(k, curr_window):
            ans += 1

print(ans)
