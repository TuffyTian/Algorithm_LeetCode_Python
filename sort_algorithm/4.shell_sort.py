def shell_sort(array: [int]):
    n = len(array)
    gaps = 1
    while gaps < (len(array) // 3):
        gaps = gaps * 3 + 1

    while gaps > 0:
        for i in range(gaps, n):
            j = i
            while j > gaps - 1 and array[j] < array[j - gaps]:
                tem = array[j]
                array[j] = array[j - gaps]
                array[j - gaps] = tem
                j = j - gaps
        gaps = (gaps - 1) // 3
    return array


if __name__ == "__main__":
    nums = [5, 4, 6, 3, 9, 2, 10, 32, 33]
    print(shell_sort(nums))