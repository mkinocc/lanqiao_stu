# DFS
def dfs(s, e, mylist, visited):
    # 如果起始点地址和终点地址一样，则返回-1
    if s == e:
        flag = True
        return 0
    for i in path[s]:
        if not visited[i] or i == -1:
            continue



if __name__ == '__main__':
    # 站点数，通道数
    n, m = map(int, input().split())

    # 创建邻接表存储
    # 下标0不能用，然后是n个站点，所以是创建n + 1行
    path = [[] for j in range(n + 1)]

    for i in range(m):
        u, v = map(int, input().split())
        path[u].append(v)
        path[v].append(u)
    u, v = map(int, input().split())

    # 初始化访问标记
    visited = [False] * (n + 1)

    flag = False

    dfs(u, v, path, visited)

    if not flag:
        print(-1)
    else:
        pass





