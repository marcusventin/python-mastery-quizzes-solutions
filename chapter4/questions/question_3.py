# Write a program that:
# * Calculates the first 20 Fibonacci numbers.
#   * The first Fibonacci number is 0.
#   * The second Fibonacci number is 1.
#   * Every Fibonacci number after that is calculated by adding the
#     previous two Fibonacci numbers together e.g. the third Fibonacci
#     number is the result of `0 + 1`.
# * prints these numbers, one per line.

def fib_nums(num):
    nums = [0, 1]
    while len(nums) < num:
        nums.append(nums[-1] + nums[-2])
    
    for number in nums[:num]:
        print(number)

fib_nums(20)
