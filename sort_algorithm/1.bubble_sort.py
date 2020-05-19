def bubble_sort(nums: [int]):
    """
    For bubble sort the time complexity is O(n^2)
    冒泡排序的时间复杂度是O(n^2)， 每一次都从最下层选择最小的冒到最上面。
    """
    n = len(nums)
    for i in range(n):
        for j in range(n, i, -1):
            # compare from the last two elms, if the back element is lesser than the front onem then change them
            # 从最后面两个元素开始比较,如果后面的元素小于前面的元素，那个就将两个元素交换
            if nums[j - 1] < nums[j - 2]:
                nums[j - 2], nums[j - 1] = nums[j - 1], nums[j - 2]
    return nums


if __name__ == "__main__":
    num = [1, 3, 5, 2, 7, 4]
    print(bubble_sort(num))
