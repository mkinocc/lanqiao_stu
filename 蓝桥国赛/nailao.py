# 并查集
# 两点变为两个小球
# 只有当两个小球之间的举例小于等于 r * 2
# 也就是相切或者是相交的时候才能穿越
def distance(x1, y1, z1, x2, y2, z2):
    # 计算两点之间的欧几里得距离
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5


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
    T = int(input())
    for _ in range(T):
        # 空洞的数量 奶酪的高度 空洞的半径
        n, h, r = map(int, input().split())
        tmp = []
        for _ in range(n):
            t = list(map(int, input().split()))
            tmp.append(t)

        fa = [0] * 10 ** 9
        init(n)

        if distance(tmp[0][0], tmp[0][1], tmp[0][2], tmp[1][0], tmp[1][1], tmp[1][1]) <= 2 * r:
            pass

        tmp = []
