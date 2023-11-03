from itertools import permutations

def check_condition(numbers, condition):
    con = ''
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            con += '>'
        else:
            con += '<'
    return con == condition

# Read input
N = int(input())
condition = input().strip()

numbers = tuple(range(1, N + 1))
del N
permutations_list = list(permutations(numbers)) # set of all permutations of mo
del numbers

count = 0
for perm in permutations_list:
    if check_condition(perm, condition):
        count += 1

print(count)
