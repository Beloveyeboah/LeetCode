#!/usr/bin/python3

"""
Given an integer num, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it
by 2, otherwise, you have to subtract 1"""

def steps_to_zero(num: int)->int:

    count = 0
    while num / 2 != 0:
        if num % 2 == 0:
            num = num / 2
            count += 1
        else:
            num = num - 1
            count += 1
    return count


num = 14
n = steps_to_zero(num)
print(n)
