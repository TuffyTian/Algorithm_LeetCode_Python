"""
 * @Author: TuffyTian 
 * @Date: 2020-05-20 19:04:08 
 * @Last Modified by:   TuffyTian 
 * @Last Modified time: 2020-05-20 19:04:08 
"""


# 选择排序  每次一个最小值放入到数组的第一位
def selection_sort(nums: [int]) -> [int]:
    # The selection sort's time complexity is O(n^2), every round of loop to select the lessest element. and chane with the top one
    # 关于选择排序，每一次的遍历我们都选择一个最小的元素，然后最上层的元素进行交换。
    n = len(nums)
    for i in range(n):
        # current to point to the smallest emement's index.
        # 一个游标，指向元素中最小元素的位置
        current: int = i
        for j in range(i + 1, n):
            if nums[j] < nums[current]:
                current = j
        # after round we should exchange the position of i and current the smallest one
        # 经过一轮的循环，我们需要交换，最当前i的元素和目前循环一轮中最小的元素。
        nums[i], nums[current] = nums[current], nums[i]
    return nums


if __name__ == "__main__":
    num = [1, 4, 6, 3, 9, 2]
    print(selection_sort(num))
