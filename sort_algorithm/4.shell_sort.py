class Resolution:
    def shell_sort(self, nums: [int]):
        n = len(nums)
        gaps = 1
        while gaps < (len(nums) // 3):
            gaps = gaps * 3 + 1

        while gaps > 0:
            for i in range(gaps, n):
                j = i
                while j > gaps - 1 and nums[j] < nums[j - gaps]:
                    tem = nums[j]
                    nums[j] = nums[j - gaps]
                    nums[j - gaps] = tem
                    j = j - gaps
            gaps = (gaps - 1) // 3
        return nums


if __name__ == "__main__":
    nums = [5, 4, 6, 3, 9, 2, 10, 32, 33]
    print(Resolution().shell_sort(nums))