"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)
if len(numbers)%2 == 0:
    x = len(numbers)//2
    y = numbers[x] - numbers[x-1]
    y = y/2
    median = numbers[x-1] + y
    print(median)
else:
    median = numbers[len(numbers)//2]
    print(median)

