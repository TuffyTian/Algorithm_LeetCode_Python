"""
 * @Author: TuffyTian 
 * @Date: 2020-06-07 15:31:03 
 * @Last Modified by:   TuffyTian 
 * @Last Modified time: 2020-06-07 15:31:03 

 二分查找算法。
 要求： 要查找的数组是已经排序好的数组
"""


def binary_search(arr: [int], find_val: int):
    left = 0
    right = len(arr)
    index = -1

    while left < right:
        mid = (right + left + 1) // 2
        if arr[mid] < find_val:
            left = mid
        elif arr[mid] > find_val:
            right = mid
        elif arr[mid] == find_val:
            index = mid
            break
    return index


if __name__ == "__main__":
    array = [1, 4, 5, 8, 10, 22, 44]
    index = binary_search(array, 22)
    print(index)
