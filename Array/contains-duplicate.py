"""
Contains Duplicate (LeetCode 217)

Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.
"""


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))


if __name__ == "__main__":
    s = Solution()
    assert s.containsDuplicate([1, 2, 3, 1]) is True
    assert s.containsDuplicate([1, 2, 3, 4]) is False
    assert s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
    assert s.containsDuplicate([1]) is False
    print("All tests passed.")
