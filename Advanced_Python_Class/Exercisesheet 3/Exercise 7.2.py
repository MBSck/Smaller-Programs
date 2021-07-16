class Fibonacci:
    def __init__(self, limit):
        self.limit = limit
        self.fib_list = []

    def __contains__(self, item):
        for fib_value in Fibonacci(self.limit):
            self.fib_list.append(fib_value)
        return item in self.fib_list

    def __getitem__(self, item):
        if item > self.limit:
            raise IndexError("Index is out of bounds")

        for fib_value in Fibonacci(self.limit):
            self.fib_list.append(fib_value)

        return self.fib_list[item]

    def __iter__(self):
        self.a, self.b = 0, 1
        self.n = 0
        while self.n <= self.limit:
            yield self.a
            self.a, self.b = self.a + self.b, self.a
            self.n += 1



if __name__ == "__main__":
    for i in Fibonacci(9):
        print(i, end=", ")

    print()
    print(5 in Fibonacci(9))
    fib = Fibonacci(9)
    print(fib[6])
    print(sum(Fibonacci(10)))
