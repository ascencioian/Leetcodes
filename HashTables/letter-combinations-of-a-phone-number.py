class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        result: list[str] = []

        def backtrack(i: int, path: list[str]) -> None:
            if i == len(digits):
                result.append("".join(path))
                return
            for c in mapping[digits[i]]:
                path.append(c)
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return result


if __name__ == "__main__":
    s = Solution()
    assert s.letterCombinations("") == []
    assert sorted(s.letterCombinations("2")) == ["a", "b", "c"]
    assert sorted(s.letterCombinations("23")) == [
        "ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"
    ]


  