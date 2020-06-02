import math


def find_median_sorted_array(nums1: [int], nums2: [int]):
    m = len(nums1)
    n = len(nums2)

    # if length of nums1 is greater than length of nums2, we exchange them and m, n for convenience
    if (m > n):
        nums1, nums2, m, n = nums2, nums1, n, m

    # the number of left element.
    total_left = (m + n + 1) // 2
    # we should just see the nums1
    left = 0
    right = m
    # initialize the max_numbers and min_numbers
    max_left_of_nums1, min_right_of_nums1, max_left_of_nums2, min_right_of_nums2 = 0, 0, 0, 0

    while left < right:
        # the middle of nums1, i is on the right of divider of nums1.
        i = (left + right + 1) // 2
        # j is the middle of nums2. j is on the right of divider of nums2
        j = total_left - i

        # consider the eage of nums,
        # if i == 0, it's out of the left edge of nums1, we should set max_left_of_nums1 to be -infinite
        max_left_of_nums1 = -math.inf if i == 0 else nums1[i-1]
        # if i == m, it's out of the right edge of nums1, we should set min_right_of_nums1 to be infinite
        min_right_of_nums1 = math.inf if i == m else nums1[i]
        # if j == 0, it's out of the left edge of nums2, we should set max_left_of_nums2 to be -infinite
        max_left_of_nums2 = -math.inf if j == 0 else nums2[j - 1]
        # if j == n, it's out of the right edge of nums2, we should set min_right_of_nums2 to be infinite
        min_right_of_nums2 = math.inf if j == n else nums2[j]

        # compare max_left_of_nums1 to min_right_of_nums2
        if max_left_of_nums1 > min_right_of_nums2:
            # i - 1 is really important
            right = i - 1
        elif max_left_of_nums1 <= min_right_of_nums2 and max_left_of_nums2 > min_right_of_nums1:
            left = i
        else:
            break

    i = (left + right + 1) // 2
    j = total_left - i
    max_left_of_nums1 = -math.inf if i == 0 else nums1[i-1]
    min_right_of_nums1 = math.inf if i == m else nums1[i]
    max_left_of_nums2 = -math.inf if j == 0 else nums2[j - 1]
    min_right_of_nums2 = math.inf if j == n else nums2[j]

    # if m + n is odd number we just see the max one of left of nums1 and nums2
    if (m + n) % 2 == 1:
        return max(max_left_of_nums1, max_left_of_nums2)
    # otherwise we should see the average of max_left and min_right
    else:
        return (max(max_left_of_nums1, max_left_of_nums2) + min(min_right_of_nums1, min_right_of_nums2)) / 2.0


if __name__ == "__main__":
    nums1 = [3]
    nums2 = [-2, -1]
    median = find_median_sorted_array(nums1, nums2)
    print(median)
