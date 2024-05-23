if __name__ == '__main__':
    # S = str(input())
    # T = str(input())
    #
    # ans = 0
    # # 定义一个临时的变量用来存储下标
    # index_t = S.find(T[0])
    # if index_t != -1:
    #     # 查询了第一个字符存在就先加一个1
    #     ans += 1
    #     for i in range(1, len(T)):
    #         # 定义查询的位置从上次查到位置之后,index_t是可以闭区间
    #         index_t = S.find(T[i], index_t + 1)
    #         if index_t == -1:
    #             continue
    #         ans += 1
    # print(ans)


    S = input()
    T = input()
    count = 0
    for i in range(len(S)):
        if S[i] == T[count]:
            count += 1
    print(count)
