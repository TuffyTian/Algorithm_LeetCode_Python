def insertion_sort(nums: [int]):
    """
    In every round loop, we will sort the part of the front,
    每一次的循环，我们都会将前一部分排列好。
    """
    n = len(nums)
    # we will begin with the second element, cause we can think the first element that has been sorted
    # 我们将从第二个元素进行排序，因为第一个元素我们可以看作已经排序好了。
    for i in range(1, n):
        # Get the current element that needs to be sorted
        # 拿到当前需要排序的元素
        temp = nums[i]
        # we should compare the current element with the elemnts which have been sorted.
        # 我们需要拿当前需要排序的元素与前面排序好的元素进行一一比较
        for j in range(0, i):
            # if the temp is lesser, we should exchange them. otherwise we will break, because the elements have been sorted
            # 如果当前的元素比较小，我们就交换他们，否则就直接结束循环，因为这些元素已经被排序好了。
            if temp < nums[i - j - 1]:
                nums[i - j] = nums[i - j - 1]
            else:
                nums[i - j] = temp
                break
    return nums


if __name__ == "__main__":
    nums = [1, 4, 6, 3, 9, 2]
    print(insertion_sort(nums))