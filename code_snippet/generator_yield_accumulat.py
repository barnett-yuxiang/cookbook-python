def accumulate(numbers):
    total = 0
    for number in numbers:
        total += number
        yield total
    
numbers = [1, 2, 3, 4, 5]

generator = accumulate(numbers)

print(next(generator))  # 1
print(next(generator))  # 3
print(next(generator))  # 6
print(next(generator))  # 10
print(next(generator))  # 15
print(next(generator))  # StopIteration
