# 希尔排序其实就是插入排序的升级版本，插入排序每次的增量是1. 最坏的情况是每一次的循环都要执行n(1+n)/2次
# 希尔排序会首先设置一个增量，每次排序完就缩小这个增量。然后最后缩小为1
# shell sort is a optimized version of insert sort. we set a gap first to compare the elements with this gap.
# finally the gap will be 1. just like the insert sort
def shell_sort(array: [int]):
    n = len(array)
    # first we set the gap to be half of the count of array.
    # 我们一般把增量设置为数组的一半
    gaps = (n+1) // 2

    while gaps > 0:
        # 下面就是正常的插入排序的逻辑
        # it's just same as insertion sort
        for i in range(gaps, n):
            while i > gaps - 1 and array[i] < array[i - gaps]:
                array[i], array[i-gaps] = array[i-gaps], array[i]
                # 记住这一步是向前走。
                i = i - gaps
        # reduce gaps
        gaps = gaps // 2
    return array


if __name__ == "__main__":
    nums = [5, 4, 6, 3, 9, 2, 10, 32]
    print(shell_sort(nums))
