# 查询, 加入路径压缩
# 动态修改x的父结点的父亲结点，包括x的父结点
def find_fa(x):
    if x != fa[x]:
        return find_fa(fa[x])
    # 如果没有加入其他组，就返回他自己
    return fa[x]

def merge_fa(x, y):
    # 寻找x的祖先,在寻找的过程中动态压缩路径
    x = find_fa(x)
    # x的祖先不一定是fa[x]
    y = find_fa(y)
    # 将x的祖先变成y
    fa[x] = y

# 初始化操作
def init(n):
    for i in range(1, n + 1):
        # 初试化每个结点的父亲结点为本身
        fa[i] = i


if __name__ == '__main__':
    n = int(input())

    # 定义fa的初始内存
    fa = [0] * 10 ** 6
    init(n)
