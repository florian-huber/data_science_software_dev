import random

def integer_division(dividend, divisor):
    quotient = 0
    while dividend >= divisor:
        dividend -= divisor
        quotient += 1
    return quotient


if __name__ == "__main__":
    for i in range(10):
        dividend = random.randint(0, 100)
        divisor = random.randint(0, 7)
        print(f"{dividend} divided by {divisor} is {integer_division(dividend, divisor)}.")
