student_nums, award_nums = map(int, input().split())
scores = list(map(int, input().split()))

if len(scores) > student_nums:
    print('학생 수와 점수 개수가 일치하지 않습니다.')

scores.sort(reverse=True)
print(scores[award_nums-1])