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
    right = len(arr) - 1
    index = -1

    while left < right:
        mid = (right + left) // 2
        if arr[mid] < find_val:
            left = mid + 1
        elif arr[mid] > find_val:
            right = mid - 1
        elif arr[mid] == find_val:
            index = mid
            break
    return index


if __name__ == "__main__":
    array = [1, 4, 5, 8, 10, 22, 44]
    index = binary_search(array, 20)
    print(index)
