"""
Valid Anagram (LeetCode 242)

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An anagram is formed by rearranging the letters of a word or phrase, using all the
original letters exactly once.
"""

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)


if __name__ == "__main__":
    sol = Solution()
    assert sol.isAnagram("anagram", "nagaram") is True
    assert sol.isAnagram("rat", "car") is False
    assert sol.isAnagram("a", "a") is True
    assert sol.isAnagram("ab", "ba") is True
    assert sol.isAnagram("abc", "abd") is False
    assert sol.isAnagram("", "") is True
    assert sol.isAnagram("a", "ab") is False
    print("All tests passed.")
