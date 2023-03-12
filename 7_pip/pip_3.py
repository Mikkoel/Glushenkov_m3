import time
def count_of_notexplostion(N: int) -> int:
    boom = [1, 2, 4]
    for i in range(3, N + 1):
        boom.append(boom[i - 1] + boom[i - 2] + boom[i - 3])
    return boom[N]

print(count_of_notexplostion(4))


def count_of_notexplostion_min(N: int) -> int:
    boom = [1, 2]
    for i in range(2, N + 1):
        boom.append(boom[i - 1] + boom[i - 2])
    return boom[N]

print(count_of_notexplostion_min(4))


def fib_dynamic(n: int) -> int:
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i - 1] + [i - 2])
    return fib[n]

start = time.time()
print(fib_dynamic(2600))
end = time.time()
print(end - start)


