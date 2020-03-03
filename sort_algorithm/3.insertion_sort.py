class Resolution:
    def insertion_sort(self, nums: [int]):
        n = len(nums)
        temp = 0
        for i in range(1, n):
            temp = nums[i]
            for j in range(0, i):
                if temp < nums[i - j - 1]:
                    nums[i - j] = nums[i - j - 1]
                else:
                    nums[i - j] = temp
                    break
        return nums


if __name__ == "__main__":
    nums = [1, 4, 6, 3, 9, 2]
    print(Resolution().insertion_sort(nums))