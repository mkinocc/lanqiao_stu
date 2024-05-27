def fun(x):
    if x == 0:
        return False
    x1 = int(x ** 0.5)
    return x1 * x1 == x


# 逐位检查每一个数字
# def fun2(x):
#     for char in x:
#         if not fun(int(char)):
#             return False
#     return True


a, b = map(int, input().split())

for i in range(a, b + 1):
    if not fun(i):
        continue
    s = str(i)
    for j in range(len(s)):
        # if fun2(s):
        #     print(i)
        #     break
        # 在切分字符串之前，检查j + 1是否在范围内，以避免切片操作中的错误
        if j + 1 < len(s) and fun(int(s[:j + 1])) and fun(int(s[j + 1:])):
            print(i)
            break
