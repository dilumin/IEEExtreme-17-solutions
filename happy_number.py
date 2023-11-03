def is_happy_number(n):
    def num_square_sum(num):
        square_sum = 0
        while num:
            square_sum += (num % 10) ** 2
            num //= 10
        return square_sum

    slow, fast = n, n
    while True:
        slow = num_square_sum(slow)
        fast = num_square_sum(num_square_sum(fast))
        if slow == fast:
            break

    return slow == 1

def count_happy_numbers(a, b):
    count = 0
    for num in range(a, b + 1):
        if is_happy_number(num):
            count += 1
    return count

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(count_happy_numbers(a, b))
