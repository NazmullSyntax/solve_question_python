#Given an m-by-n matrix with positive integers, determine the length of the longest path of increasing within the matrix. For example, consider the input matrix:
def longest_increasing_path(matrix):
    if not matrix:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])

    # dp[r][c] = longest increasing path starting from (r, c)
    dp = [[0] * cols for _ in range(rows)]

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def dfs(r, c):
        if dp[r][c] != 0:
            return dp[r][c]

        longest = 1

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if (0 <= nr < rows and
                0 <= nc < cols and
                matrix[nr][nc] > matrix[r][c]):

                longest = max(longest, 1 + dfs(nr, nc))

        dp[r][c] = longest
        return longest

    answer = 0

    for r in range(rows):
        for c in range(cols):
            answer = max(answer, dfs(r, c))

    return answer


matrix = [
    [9, 9, 4],
    [6, 6, 8],
    [2, 1, 1]
]

print("Longest Increasing Path:", longest_increasing_path(matrix))