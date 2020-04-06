def bubble_sort(nums: [int]):
    n = len(nums)
    for i in range(n):
        for j in range(n - i - 1):
            if nums[n - j - 1] < nums[n - j - 2]:
                temp = nums[n - j - 1]
                nums[n - j - 1] = nums[n - j - 2]
                nums[n - j - 2] = temp
    return nums


if __name__ == "__main__":
    num = [1, 3, 5, 2, 7, 4]
    print(bubble_sort(num))
