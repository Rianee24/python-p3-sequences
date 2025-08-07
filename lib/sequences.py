#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0 :
        print([])
        return
    fib_seq = [0, 1]
    while len(fib_seq) < length:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    print(fib_seq[:length])
    pass