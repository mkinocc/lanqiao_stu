N, M = map(int, input().split())
# 这个题目一开始理解错了， 起点和终点可以相同，但是中间经过的点不能相同， 做这题先把邻接表画出来

# 创建二维数组，当作邻接表
# 建立的是N+1阶数的，0下标的不使用
path = [[] for i in range(N + 1)]

for i in range(M):
    u, v = map(int, input().split())
    # 给邻接表负值
    path[u].append(v)
    path[v].append(u)


ans = 0
# 开始遍历邻接表
for i in range(1, N + 1):
    # 遍历邻接表的每一行
    for a in path[i]:
        # 遍历每一个出度, 找到出度所在的那一行，然后开始比较
        for b in path[a]:
            # 如果和起点不同
            if b != i:
                ans += len(path[b]) - 1  # 我们将计数器 ans 增加上顶点 b 的相邻顶点(也就是链接到b为顶点的那一行)数量减去 1
                # 这里减去 1 是因为我们不考虑回到顶点 i 的情况，避免了重复计数。

print(ans)


