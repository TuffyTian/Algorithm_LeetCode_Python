"""
 * @Author: TuffyTian 
 * @Date: 2020-06-06 19:11:14 
 * @Last Modified by:   TuffyTian 
 * @Last Modified time: 2020-06-06 19:11:14 

八皇后问题：8*8的棋盘，放皇后，两个皇后不能在同一行和同一列，也不能是对角线。一共多少种放法。
使用递归回溯解法
 """

import math

count = 8
# 初始化结果数组，init the result array
result = [math.inf for i in range(count)]
# 记录一种多少种结果. record the number of results
count_of_result = 0


# put the queen, max * max matrix
def tye_put(index: int, max: int):
    global count_of_result
    # 递归结束的条件，如果皇后全部防止完，退出递归
    # the end condition of recursion
    if index == max:
        print(result)
        count_of_result += 1
        return
    else:
        # 从0到max不停的尝试放置. from 0 to max to change the position of the queen
        for i in range(max):
            # 将当前的位置保存到结果数组中
            result[index] = i
            # 判断当前方式是否OK
            if is_ok(index, result):
                # 如果OK则开始放置下一个皇后
                tye_put(index + 1, max)


# 判断当前的放置是否OK
def is_ok(index: int, result: [int]):
    # 对比当前皇后和前面几个已经放置好的皇后
    for j in range(index):
        # 如果在同一列，或者在对角线上，则返回false， 否则返回true
        if result[j] == result[index] or abs(result[index] - result[j]) == abs(index - j):
            return False
    return True


if __name__ == "__main__":
    tye_put(0, count)
    print(count_of_result)
