#from sys import maxunicode
import sys
from collections import Counter

#count = int(input())
count = int(sys.stdin.readline())
nums = []
if count / 2 == 0 or count == 0:
    print('input error')

for i in range(count):
    #nums.append(int(input()))
    nums.append(int(sys.stdin.readline()))
    if nums[i] > 4000:
        print('input error')

nums.sort()

# 산술평균: N개의 수들의 합을 N으로 나눈 값
print(round(sum(nums)/count))

# 중앙값: N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
print(nums[count // 2])

# 최빈값: N개의 수들 중 가장 많이 나타나는 값
counter = Counter(nums).most_common()
if len(nums) > 1:
    if counter[0][1] == counter[1][1]:
        print(counter[1][0])
    else:
        print(counter[0][0])
else:
    print(counter[0][0])


# 범위: N개의 수들 중 최댓값과 최솟값의 차이
print(max(nums) - min(nums))


# ===================
# 최빈값_이전 코드(시간초과)
# nums_dic = {}
# for i in nums:
#     nums_dic[i] = nums.count(i)

# max_exist = max(nums_dic.values())  # 젤 높은 빈도수

# max_num = []
# for key, value in nums_dic.items():
#     if value == max_exist:
#         max_num.append(key)

# if len(max_num) > 1: 
#     max_num.sort()
#     print('최빈값: ', max_num[1])
# else:
#     print('최빈값: ', max_num[0])