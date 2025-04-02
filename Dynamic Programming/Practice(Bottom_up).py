#Fibonacci using Bottom Up DP

def fibonacci(n):
    #* This function calculates the nth Fibonacci number using a bottom-up dynamic programming approach.
    #* It uses an array to store the Fibonacci numbers up to n, allowing for efficient computation.
    #* The Fibonacci sequence is defined as:
    #* F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) for n >= 2.
    #* The time complexity of this approach is O(n), and the space complexity is also O(n).
    

    if n <= 1:#* Base case: if n is 0 or 1, return n directly.
        return n
    
    dp = [0] * (n + 1)#* Create an array to store Fibonacci numbers up to n.
    dp[1] = 1#* Initialize the first two Fibonacci numbers.

    for i in range(2, n + 1):#* Iterate from 2 to n.
        dp[i] = dp[i - 1] + dp[i - 2]#* Calculate the Fibonacci number at index i by summing the two preceding numbers.

    return dp[n]#* Return the nth Fibonacci number.