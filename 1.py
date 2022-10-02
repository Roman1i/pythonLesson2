n = input()
sum = 0

for i in range(len(n)):
    if n[i].isdigit():
        sum += int(n[i])

print(sum)


