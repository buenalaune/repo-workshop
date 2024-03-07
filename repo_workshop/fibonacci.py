class Fibonacci:
    def __init__(self):
        self.mem = {
            0: 0,
            1: 1
        }

    def fib(self, n: int) -> int:
        if n < 0:
            return 'Fibonacci number is not defined for negative n'
        if n in self.mem:  # Base case
            return self.mem[n]
        ...  # Compute and cache the Fibonacci number
        self.mem[n] = self.fib(n - 1) + self.fib(n - 2)  # Recursive case
        ...
        return self.mem[n]
