"""
 * @Author: TuffyTian 
 * @Date: 2020-06-07 14:25:22 
 * @Last Modified by:   TuffyTian 
 * @Last Modified time: 2020-06-07 14:25:22 

 基数排序
"""


def radix_sort(arr: [int]):
    # 先确定最大值
    max_digit = max(arr)
    # 这是一个取余数的增量。123 // 1 % 10 = 3. 123 // 10 % 10 = 2. 123 // 100 % 10 = 1
    exp = 1
    length = len(arr)
    # 设置一个count数组记录每一个桶放进去的数字个数
    count = [0 for i in range(10)]
    # 初始化10个桶，每一个大小是要排序数组的大小
    buckets = [[0 for i in range(length)] for i in range(10)]

    # 开始循环遍历。只需要遍历最大数字的数字位数。如最大数1234.我们只需要遍历4次
    while max_digit // exp > 0:
        arr = counting_sort(arr, exp, count, buckets)
        exp *= 10
    return arr


def counting_sort(arr: [int], exp: int, count: [int], buckets: [[int]]):
    length = len(arr)
    # 数组经过这一轮排序的新数组
    output = []
    # 遍历要排序的数组
    for i in range(0, length):
        # 取出当前的位数
        position_digit = arr[i] // exp % 10
        # 放入对应的桶中
        buckets[position_digit][count[position_digit]] = arr[i]
        # 该桶中的数字加1 + 1
        count[position_digit] += 1

    # 遍历桶，把里面的数字拿出来组成新的数组
    for i in range(10):
        last_count = count[i]
        for j in range(last_count):
            # 循环取出桶中的数字
            output.append(buckets[i][j])
            # 数量-1
            count[i] -= 1

    return output


if __name__ == "__main__":
    array = [33, 69, 77, 21, 10, 11, 33, 36, 39, 66, 44, 22, 123]
    array = radix_sort(array)
    print(array)
