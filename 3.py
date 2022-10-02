n = int(input())
nums = []
sum = 0

for i in range(n):
    nums.append((1 + 1 / (i + 1)) ** (i + 1))
    sum += nums[i]

print(round(sum, 3))
