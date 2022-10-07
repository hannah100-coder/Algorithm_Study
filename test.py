# 파이썬 기본 문법 정리

print("hello world")

# 변수 선언
a = "hihi"
print(type(a))  # <class 'str'>
a = 3
print(type(a))  # <class 'int'>

# 입력 받기
name = input('name: ')
print(name)

# 리스트
empty_list = []
fruits = ['apple', 'banana', 'watermelon']

# 리스트에 데이터 추가
students = []
student_name = '백혜윤'
students.append(student_name)
print(students)

# 리스트 데이터 불러오기
alphabet = ['A', 'B', 'C', 'D']
print(alphabet[0])  # 리스트의 0번 인덱스에 해당하는 데이터 출력
print(alphabet[-1]) # 리스트의 가장 마지막 인덱스 출력
print(alphabet[0:2])# 리스트의 0번부터 2번 전까지의 데이터 출력
print(alphabet[1:]) # 리스트 1번부터 끝까지 출력
print(len(alphabet)) # 리스트 엘리먼트 갯수 출력
print(alphabet.index('C'))  # 특정 엘리먼트 인덱스 찾기

# 리스트 오름차순 정렬
x = [4, 6, 2, 9]
y = sorted(x)
print(y)    # [2, 4, 6, 9]

n = ['jack', 'sarah', 'anna']
s = sorted(n)
print(s)    # ['anna', 'jack', 'sarah']

# min, max, sum
x = [100, 300, 20, 3]
print(min(x))   # 3
print(max(x))   # 300
print(sum(x))   #423

# 이차원 배열
names = ['홍길동', '백혜윤', '전수민']
scores = [10, 70, 90]
set = [names, scores]
print(set)  # [['홍길동', '백혜윤', '전수민'], [10, 70, 90]]
print(set[1][1])    # 70

# 딕셔너리
# : key와 values로 이루어지며, key는 불변하는 값만 넣을 수 있음
dic = {'apple' : 1 , 'banana' : 2, 'grape' : 3}
print(dic)

phone_dic = {}
phone_dic['홍길동'] = '010-123'
phone_dic['백혜윤'] = '010-456'
phone_dic['전수민'] = '010-789'
print(phone_dic)    
# {'홍길동': '010-123', '백혜윤': '010-456', '전수민': '010-789'}

info_dic = {}
info_dic['name'] = '홍길동'
info_dic['phone'] = '010-123'
info_dic['address'] = 'Seoul'
print(info_dic)
# {'name': '홍길동', 'phone': '010-123', 'address': 'Seoul'}

# 딕셔너리 키 값, 밸류 값 체크
dic = {'apple' : 1 , 'banana' : 2, 'grape' : 3}
print(dic.keys())   # dict_keys(['apple', 'banana', 'grape'])
print(dic.values()) # dict_values([1, 2, 3])

# 조건문 _ 들여쓰기, 대소문자 구분 중요!
if 2 > 1:
    print("it's true")

if not 1 > 2:
    print("it's false")

a = 1
b = 2
if a+b < 3:
    print('a+b<3 입니다')
elif a+b == 3:
    print('a+b=3 입니다')
else:
    print('a+b>3 입니다')

# 반복문
for i in range(2, 10):
    for j in range(1, 10):
        print('%d x %d = %d' %(i, j, i*j))

area = ['서울', '대전', '대구', '부산']
for i in area:
    print(i)

i = 0
while True:
    i += 1
    if i == 2:
        continue
    if i > 4:
        break
    print("let's go %d" %(i))

# 예외 처리
try:
    print(100/0)    # 예외로 인해 에러가 날 수도 있는 코드를 try 안에 작성.
                    # 에러가 나도 멈추지 않고 다음 코드를 실행함.
except:
    print("100은 0으로 나눌 수 없습니다")   # 예외가 발생한 경우 처리
finally:
    print("다음 작업을 실행합니다") # 에러 발생 여부와 상관없이 무조건 실행되는 구문 필요시


# 람다 함수
plus_ten = lambda x : x+10
print(plus_ten(3))  # 13

# 함수
def multiply(num):
    for i in range(1,10):
        print(num, 'x', i, '=', num*i)
    

multiply(5) # 5단 출력