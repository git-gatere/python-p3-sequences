#!/usr/bin/env python3

def print_fibonacci(length):
    sequence = []
    sequence.append(0)
    sequence.append(1)
    
    while len(sequence) < length :
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence[0:length]
    
print(print_fibonacci(9))