number = input()
numbers = [int(x) for x in number]
numbers.sort(reverse=True)

for num in numbers:
    print(num,end='')
