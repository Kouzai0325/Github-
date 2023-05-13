numbers = [1, 2, 4, 7]
for number in numbers:
    mod = number % 2
    if mod == 0:
        print(str(number) + 'は偶数')
    else:
        print(str(number) + 'は奇数')