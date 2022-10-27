class FibonacciDynamicMemoization:
    def fibonacci(n):
        # Base case: n = 0 or 1
        if n <= 1:
            return n

        # Recursive case: fib(n) = fib(n - 1) + fib(n - 1)
        return FibonacciDynamicMemoization.fibonacci(n - 1) + FibonacciDynamicMemoization.fibonacci(n - 2)

    # Memoization
    def fibonaccimemoization(n, cache):
        if n <= 1:
            return n
        if n in cache:
            return cache[n]

        cache[n] = FibonacciDynamicMemoization.fibonaccimemoization(n - 1, cache) + FibonacciDynamicMemoization.fibonaccimemoization(n - 2, cache)
        return cache[n]

    # Dynamic Programming
    def fibonaccidp(n):
        if n < 2:
            return n

        dp = [0, 1]
        i = 2
        while i <= n:
            tmp = dp[1]
            dp[1] = dp[0] + dp[1]
            dp[0] = tmp
            i += 1
        return dp[1]
    
if __name__ == '__main__':
    print(FibonacciDynamicMemoization.fibonaccidp(6))
    print(FibonacciDynamicMemoization.fibonaccimemoization(6, {}))
