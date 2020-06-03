# find the longest palindromic substring
# we have 3 ways to do it

# first way brute_force_method
def brute_force_method(s: str):
    max_length: int = 1
    begin: int = 0
    length = len(s)
    if length < 2:
        return s

    # from the first charater
    for i in range(0, length - 1):
        for j in range(i + 1, length):
            if (valid_palindromic_substring(s, i, j) and (j - i + 1) > max_length):
                max_length = j - i + 1
                begin = i
    return s[begin: begin + max_length]


# valid if the substring is a palindromic
def valid_palindromic_substring(s: str, left: int, right: int):
    while (left < right):
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


# second way is expending from center to find the palindromic
def expend_method(s: str):
    length = len(s)
    if length < 2:
        return s
    max_length = 1
    begin = 0
    for i in range(0, length):
        # handle odd condition
        odd_length = expend_around_center(s, i, i)
        # handle even condition
        even_length = expend_around_center(s, i, i + 1)
        bigger_length = max(odd_length, even_length)
        if bigger_length > max_length:
            max_length = bigger_length
            # take care
            begin = i - (max_length - 1) // 2
    return s[begin: begin + max_length]


def expend_around_center(s: str, left: int, right: int):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    # like right-left + 1 - 2. for the palindromic substr doesn't include left and right
    return right - left - 1


# the third one is to use dynamic programming
def dynamic_programming_method(s: str):
    length = len(s)
    if length < 2:
        return s
    max_length = 1
    begin = 0
    dp = [[False for i in range(0, length)] for j in range(0, length)]
    # initial the result array
    for i in range(0, length):
        dp[i][i] = True

    for j in range(1, length):
        for i in range(0, j):
            if (s[i] != s[j]):
                dp[i][j] = False
            else:
                if j - i < 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i+1][j-1]
            if dp[i][j] and j - i + 1 > max_length:
                max_length = j - i + 1
                begin = i
    return s[begin: max_length + begin]


if __name__ == "__main__":
    s = "abb"
    # sub_string = brute_force_method(s)
    sub_string = dynamic_programming_method(s)
    print(sub_string)
