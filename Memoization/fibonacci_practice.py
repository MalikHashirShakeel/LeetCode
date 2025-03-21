def memoized(n):
    memo = {}

    def fibb(n):
        if n <= 1:
            return n
        
        if n in memo:
            return memo[n]
        
        memo[n] =  fibb(n - 1) + fibb(n - 2)
        return memo[n]
    
    return fibb(n)