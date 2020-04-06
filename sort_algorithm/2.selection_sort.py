# 选择排序  每次一个最小值放入到数组的第一位
def selection_sort(nums: [int]) -> [int]:
    n = len(nums)
    for i in range(n):
        current = i
        for j in range(i + 1, n):
            if nums[j] < nums[current]:
                current = j
        temp = nums[i]
        nums[i] = nums[current]
        nums[current] = temp
    return nums


if __name__ == "__main__":
    num = [1, 4, 6, 3, 9, 2]
    print(selection_sort(num))

