"""finding the indices of array"""
def twoSum(nums, target):
    new = {}
    for x, value in enumerate(nums):
        com = target - value
        if com in new:
            return [new[com], x]
        new[value] = x
    return None

a = [2, 4, 7, 11, 15]
target = 9
b = twoSum(a, target)
print(b)
