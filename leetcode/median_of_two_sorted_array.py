def find_median_sorted_array(nums1: [int], nums2: [int]):
    nums1_length = len(nums1)
    nums2_length = len(nums2)
    left = (nums1_length + nums2_length + 1) / 2
    right = (nums1_length + nums2_length + 2) / 2
