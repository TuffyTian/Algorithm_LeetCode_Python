def partition(nums, left, right):
    pivot = nums[left]
    start = left + 1
    end = right

    while True:
        while start <= end and nums[start] <= pivot:
            start += 1

        while start <= end and nums[end] >= pivot:
            end -= 1

        if start <= end:
            nums[start], nums[end] = nums[end], nums[start]
        else:
            break

    nums[left], nums[end] = nums[end], nums[left]
    return end


def quick_sort(nums, left, right):
    if left >= right:
        return

    p = partition(nums, left, right)
    quick_sort(nums, left, p - 1)
    quick_sort(nums, p + 1, right)


if __name__ == '__main__':
    nums = [33, 69, 77, 21, 10, 11, 33, 36, 39, 66, 44, 22]

    quick_sort(nums, 0, len(nums) - 1)
    print(nums)
