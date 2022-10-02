n = int(input("N: "))
nums = []
i = 0

while i < n * 2 + 1:
    nums.append(-n + i)
    i += 1

print(nums)

a = int(input("a: "))
b = int(input("b: "))

print("result = " + str(nums[a - 1] * nums[b - 1]))