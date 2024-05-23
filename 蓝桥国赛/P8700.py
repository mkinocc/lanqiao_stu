T = int(input())
# 枚举内圈的4个位置来检查是否可以通过某种旋转或交换
# 外圈全部G， 中圈全部R， 内圈全部Y
for t in range(T):
    Out = input()
    Mid = input()
    Inn = input()

    for i in range(4):
        flag = 0
        # 使用字典统计当前内圈位置的颜色数量
        dict = {'G': 0, 'R': 0, 'Y': 0}
        # 因为当进行操作一和操作二时，进行旋转，与内圈每一个塑料棒对应的塑料棒总共有五个，中圈2个，外圈三个。分别对应中圈的下标0，4
        # 外圈的下标0 4 8

        # 统计外圈当前位置及其相隔4和8的位置的颜色
        # 枚举内圈的4个塑料棒，再记录下这6个塑料棒的颜色，再判断
        dict[Out[i]] += 1
        dict[Out[i + 4]] += 1
        dict[Out[i + 8]] += 1
        # 统计中圈当前位置及其相隔4的位置的颜色
        dict[Mid[i]] += 1
        dict[Mid[i + 4]] += 1
        # 统计内圈当前位置的颜色
        dict[Inn[i]] += 1

        # 只有当这六个塑料棒的总数为 3个绿色，2个红色， 1个黄色才可以输出YES，就是肯定可以通过操作三能得到
        if dict['G'] != 3 or dict['R'] != 2 or dict['Y'] != 1:
            flag = 1
            break
    if flag:
        print("NO")
    else:
        print("YES")