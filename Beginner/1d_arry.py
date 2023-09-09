#!/usr/bin/bash

def runsum(num):
    new = []
    sum = 0
    for i in num:
        sum += i
        new.append(sum)
    return new

a = [4, 80, 5, 6]
b = runsum(a)
print(b)
