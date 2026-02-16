def length_of_longest_substring(s: str) -> int:
    """
    Find the length of the longest substring without duplicate characters.
    Uses sliding window with a set to track characters in the current window.
    """
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.discard(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len


if __name__ == "__main__":
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
    print("All examples passed.")

# Approach: sliding window + set
# left: start of the current window.
# right: end of the current window (loop index).
# seen: set of characters in the window s[left..right].
# For each right:
# While s[right] is already in seen, remove s[left] from seen and move left right (shrink the window until it has no duplicate).
# Add s[right] to seen.
# Update the best length with right - left + 1.
# Time: O(n) — each index is processed at most twice (once by right, once by left).
# Space: O(min(n, alphabet size)) for the set.
# All three examples pass when you run the file.
