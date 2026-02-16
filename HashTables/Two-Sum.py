from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Return indices of the two numbers in nums that add up to target.
    Uses a single pass with a hash map: for each num, check if (target - num)
    was seen before; if so return [that index, current index].
    """
    seen: dict[int, int] = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return [] 
    


# Examples
if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    print("All examples passed.")
