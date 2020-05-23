class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        result = 0
        box: map = {}
        index = 0
        for i in range(0, n):
            if s[i] in box:
                index = max(box[s[i]], index)
            result = max(result, i - index + 1)
            box[s[i]] = i + 1
        return result


if __name__ == "__main__":
    str = "abcadxyzopbb"
    print(Solution().lengthOfLongestSubstring(str))