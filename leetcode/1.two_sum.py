class Solution:
    def twoNum(self, nums, target):
        tmp = {}
        n = len(nums)
        for i in range(0, n):
            num = target - nums[i]
            if num not in tmp:
                tmp[nums[i]] = i
            else:
                return [tmp[num], i]


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoNum(nums, target))