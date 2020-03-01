class Resolution:
    def selection_sort(self, nums: [int]):
        current = 0
        n = len(nums)
        for i in range(n):
            current = i
            for j in range(i + 1, n):
                if nums[j] < nums[current]:
                    current = j
            temp = nums[i]
            nums[i] = nums[current]
            nums[current] = temp
        return nums


if __name__ == "__main__":
    nums = [1, 4, 6, 3, 9, 2]
    print(Resolution().selection_sort(nums))