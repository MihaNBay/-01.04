numbers = input("Введите последовательность чисел: ").split()
seen = []
for num in numbers:
    if num in seen:
        print("YES")
    else:
        print("NO")
        seen.append(num)
