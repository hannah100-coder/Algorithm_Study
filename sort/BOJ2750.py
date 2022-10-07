count = int(input())
nums = []

for i in range(count):
    nums.append(int(input()))

sorted_nums = sorted(nums)

for i in range(count):
    print(sorted_nums[i])