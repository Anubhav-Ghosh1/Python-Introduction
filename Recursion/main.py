import time
def print_till_n(a):
    if a == 0:
        return None
    a -= 1
    print_till_n(a)
    print(a)
print_till_n(10)
def fact(a):
    if a == 1:
        return 1
    return a * fact(a-1)
print(fact(5))

def fibo(n):
    dp = [-1] * (n+1)
    def helper(n):
        if n == 0 or n == 1:
            return 1
        if dp[n] != -1:
            return dp[n]
        dp[n] = (helper(n-1) + helper(n-2)) 
        return dp[n]
    
    helper(n)
    return dp[n]

start = time.time()
print(fibo(5))
print("Time ",time.time()-start)