#_*_coding: utf-8_*_
def fibonacci_sum(n, k):
    total = 0
    prev = 0
    next1 = 1
    for i in range(1, k + n + 1):
        if i >= k:
            total += prev
        prev,next1=next1,prev+next1
    return total


print(fibonacci_sum(int(input()), int(input())))