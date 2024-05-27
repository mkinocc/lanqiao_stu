# 知识点：并查集
# 找组长
def find_leader(x):
    # 如果植物不等于当前所属的植物的组 我们就去找他当前属于的组（递归）
    # 解释上面一句话： 初始状态 1植物属于1组，2植物属于2组，如果我们输入a b时，也就是在此时修改了当前植物所属于的组
    # 把a归并到b组或者是把b归并到a组都可以，也就是在此时修改了当前所属于的组
    if x != zhiwu[x]:
        return find_leader(zhiwu[x])
    # 如果没有加入其他组，就返回他自己
    return zhiwu[x]


if __name__ == '__main__':
    # 终于理解了这题了，两个元素之间相连就等于一个植物，同时也允许植物之间连接的传递，2-4、4-5.也就是
    # 说2 4 5都是一个合根植物
    # 同时一个植物不和任何植物相连接也是属于一个合根植物

    # 上标也就是值： 1 2 3 4 5 6 7 8 9
    # 下标就是索引： 1 2 3 4 5 6 7 8 9
    # 索引是不好修改的， 就返回修改上标
    m, n = map(int, input().split())
    k = int(input())

    zhiwu = [0] * 10 ** 6
    for i in range(1, m * n + 1):
        zhiwu[i] = i

    for i in range(k):
        a, b = map(int, input().split())
        # 找a ，b植物的上标
        a_fa = find_leader(a)
        b_fa = find_leader(b)
        # 将a植物的上标改成b植物的上标（结合成一组）
        zhiwu[a_fa] = b_fa

    # 只有当上标和下标一致的时候，才是合根植物
    ans = 0
    for j in range(1, len(zhiwu)):
        if j == zhiwu[j]:
            ans += 1

    print(ans)
