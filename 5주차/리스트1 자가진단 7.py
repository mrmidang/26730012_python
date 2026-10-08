numbers = []

while True:
    n = int(input())

    if n == 0:
        break

    numbers.append(n)

print(*numbers[1::2])
