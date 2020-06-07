"""
 * @Author: TuffyTian 
 * @Date: 2020-06-07 16:34:46 
 * @Last Modified by:   TuffyTian 
 * @Last Modified time: 2020-06-07 16:34:46 

 插值查找算法， 使用了递归
"""


def insertion_search(arr: [int], find_val: int, left: int, right: int):
    # 使用比例法寻找最佳的点。
    mid = left + (find_val - arr[left]) * (right - left) // (arr[right] - arr[left])
    if find_val < array[left] or find_val > array[right] or left > right:
        return - 1
    elif find_val > arr[mid]:
        return insertion_search(arr, find_val, mid + 1, right)
    elif find_val < array[mid]:
        return insertion_search(arr, find_val, left, mid - 1)
    else:
        return mid


if __name__ == "__main__":
    array = [1, 4, 5, 8, 10, 22, 44]
    index = insertion_search(array, 22, 0, len(array)-1)
    print(index)
