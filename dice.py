
from fractions import Fraction
MOD = 998244353




# Calculate q^(-1) using extended Euclidean algorithm
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 % m0

# q_inverse = mod_inverse(q, modulus)
# print(f"q^(-1) mod 998244353: {q_inverse}")


def calculate_probability(t, n):
    # Initialize a 2D array dp
  
    dp = [[0] * (6*t+1) for _ in range(t+1)]
    
   
    dp[0][0] = 1
    
    # Calculate the number of ways to get each sum
    for i in range(1, t+1):
        for j in range(1, 6*t+1):
            for face in range(1, 7):
                if j - face >= 0:
                    dp[i][j] += dp[i-1][j-face]
    
    
    
    probability = dp[t][n] / (6**t)
    del dp
   
    
    return probability


n,k=map(int,input().split())
probability=0
for i in range(1,k+1):
 if (n <= i*6):
   probability += calculate_probability(i, n)
 else:
     probability+=0
     

rational_number = Fraction(probability/k).limit_denominator()





q_inverse = mod_inverse(rational_number.denominator, MOD)


result = ( rational_number.numerator* q_inverse) % MOD
print(result)