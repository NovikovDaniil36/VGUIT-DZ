#-*-coding: utf-8-*-
def fibonacci(n):
    total = 0
    prev = next1 = 1
    for i in range(1, n + 1):
        total += prev
        prev, next1=next1,prev+next1
    return total


print(fibonacci(int(input())))