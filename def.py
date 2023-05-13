def loop(numbers):
    for number in numbers:
     mod = number % 2
    if mod == 0:
        print(str(number) + 'は偶数')
    else:
        print(str(number) + 'は奇数')
        return mod
    
numbers = loop(14,22,11)
print(numbers)