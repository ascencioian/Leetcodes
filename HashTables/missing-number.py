class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        # Sum of 0..n is n*(n+1)/2. Missing = expected_sum - actual_sum.
        expected = n * (n + 1) // 2
        actual = sum(nums)
        return expected - actual

    def missingNumber_set(self, nums: list[int]) -> int:
        """O(n) time, O(n) extra space: hash set of nums, then scan 0..n."""
        seen = set(nums)
        n = len(nums)
        for x in range(n + 1):
            if x not in seen:
                return x
        return -1


if __name__ == "__main__":
    sol = Solution()
    assert sol.missingNumber([3, 0, 1]) == 2
    assert sol.missingNumber([0, 1]) == 2
    assert sol.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
    assert sol.missingNumber_set([3, 0, 1]) == 2
    assert sol.missingNumber_set([0, 1]) == 2
    assert sol.missingNumber_set([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
    print("All assertions passed.")
