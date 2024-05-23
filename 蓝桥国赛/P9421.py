n = int(input())

s = list(map(int, input().split()))
# 题目要理解清楚，不是偶次数都要 而是只有次数为2的不用修改，

ans1 = 0
ans2 = 0

#减少比较次数
set_s = set(s)
for num in set_s:
    times = s.count(num)
    if times == 1:
        ans1 += 1
    elif times > 2:
        ans2 += (times - 2)

if ans1 >= ans2:
    # 这个公式是：也就是ans2里面的数全部要修改，因为次数大于2，ans2代表的数已经全部不能用了，然后可以改成ans1里面的数。
    # 然后剩余ans1里面的数要改一半，去凑自己的另一半
    print((ans1 - ans2) // 2 + ans2)
else:
    print((ans2 - ans1) + ans1)

# 不是大哥，怎么改啊，怎么总是超时啊


