class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        rows, cols = len(s), len(p)
        dp = [[False] * (cols + 1) for _ in range(rows + 1)]
        dp[rows][cols] = True

        for i in range(rows, -1, -1):
            for j in range(cols - 1, -1, -1):
                first_match = (
                    i < rows and (s[i] == p[j] or p[j] == ".")
                )

                if j + 1 < cols and p[j + 1] == "*":
                    dp[i][j] = dp[i][j + 2] or (
                        first_match and dp[i + 1][j]
                    )
                else:
                    dp[i][j] = (
                        first_match and dp[i + 1][j + 1]
                    )

        return dp[0][0]