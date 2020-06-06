
def merge_sort(self, nums: [int]):
    if len(nums) == 1:
        return nums
    n = len(nums)
    mid = n // 2
    # divide the array. to left and right
    left = nums[:mid]
    right = nums[mid:]
    return merge(self.merge_sort(left), self.merge_sort(right))


def merge(self, left: [int], right: [int]):
    result = []
    # 两个游标，分别从left数组的左边和right数组的左边开始，每次选出最小值。放入result数组中
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    result += left
    result += right
    return result


if __name__ == '__main__':
    nums = [11, 99, 33, 69, 77, 88, 55, 11, 33, 36, 39, 66, 44, 22]
    print(merge_sort(nums))
