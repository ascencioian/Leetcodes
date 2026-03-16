"""
Valid Parenthesis String (LeetCode 678)

Given a string s containing only three types of characters: '(', ')' and '*',
return true if s is valid.

Rules:
- Any left parenthesis '(' must have a corresponding right parenthesis ')'.
- Any right parenthesis ')' must have a corresponding left parenthesis '('.
- Left parenthesis '(' must go before the corresponding right parenthesis ')'.
- '*' can be treated as ')', '(', or empty string "".
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        # [lo, hi] = range of possible unmatched open '(' count
        lo = hi = 0
        for c in s:
            if c == "(":
                lo += 1
                hi += 1
            elif c == ")":
                lo = max(0, lo - 1)
                hi -= 1
                if hi < 0:
                    return False
            else:  # '*'
                lo = max(0, lo - 1)  # use as ')' or ""
                hi += 1               # use as '(' or ""
        return lo == 0


if __name__ == "__main__":
    sol = Solution()
    assert sol.checkValidString("()") is True
    assert sol.checkValidString("(*)") is True
    assert sol.checkValidString("(*))") is True
    assert sol.checkValidString("") is True
    assert sol.checkValidString("((*)") is True
    assert sol.checkValidString(")(") is False
    assert sol.checkValidString("())") is False
    assert sol.checkValidString("(((*(*))") is True
    print("All tests passed.")
