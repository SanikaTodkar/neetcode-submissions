class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        last_seen = {}

        for right in range(len(s)):
            char = s[right]

            if char in last_seen:
                left = max(left, last_seen[char] + 1)

            last_seen[char] = right

            current_length = right - left + 1

            max_length = max(current_length, max_length)

        return max_length


