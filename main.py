def longest_common_subsequence(X, Y):
    m = len(X)
    n = len(Y)

    # Create a 2D dp array to store lengths of longest common subsequence.
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the dp table using the recurrence relations.
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # The length of the LCS is stored in dp[m][n].
    lcs_length = dp[m][n]

    # To reconstruct the LCS string:
    lcs_str = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_str.append(X[i - 1])  # Add the character to the LCS
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # The LCS is constructed in reverse, so reverse it.
    lcs_str.reverse()

    return lcs_length, ''.join(lcs_str)
