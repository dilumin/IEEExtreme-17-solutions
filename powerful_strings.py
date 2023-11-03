MOD = 998244353

def count_powers(N, M, strings):
    dp = [0] * (N + 1)
    dp[0] = 1
    
    for i in range(1, N + 1):
        for string in strings:
            for j in range(len(string)):
                if i >= len(string) - j:
                    dp[i] = (dp[i] + dp[i - (len(string) - j)] * pow(2, j, MOD)) % MOD

    total_power = 0
    for i in range(1, N + 1):
        total_power = (total_power + dp[i]) % MOD

    return total_power

# Read input
N, M = map(int, input().split())
strings = [input().strip() for _ in range(M)]

# Calculate and print the result
result = count_powers(N, M, strings)
print(result)
