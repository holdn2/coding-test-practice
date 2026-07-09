# 반복문 : 특정한 소스코드를 반복적으로 실행하고자 할 때 사용하는 문법
# while 또는 for문을 사용한다.

# while
i = 1
result = 0
while i <= 9:
    result += i
    i += 1
print(result)

i = 1
result = 0
while i <= 9:
    if i % 2 == 1:
        result += i
    i += 1
print(result)

print("-------------------------------")

# for
# 특정한 변수를 이용하여 in 뒤에 오는 데이터(리스트, 튜플 등) 에 포함되어 있는 원소를 첫 번째 인덱스부터 차례대로 하나씩 방문
# for 변수 in 리스트:
array = [9, 8, 7, 6, 5]
for x in array:
    print(x)

# for문에서 연속적인 값을 차례대로 순회할 때는 range()를 주로 사용한다.
# 이 때, range(시작값, 끝값+1) 형태로 사용한다. 인자를 하나만 넣으면 시작 값이 0이 된다.
result = 0
for i in range(1, 10):
    result += i
print(result)

# continue 키워드 : 반복문에서 남은 코드의 실행을 건너뛰고, 다음 반복을 진행하고자 할 때 사용
# break : 반복문을 즉시 탈출하고자 할 때 사용

scores = [90, 85, 77, 65, 97]
cheating_student_list = {2, 4}
for i in range(5):
    if i + 1 in cheating_student_list:
        continue
    if scores[i] >= 80:
        print(i + 1, "번 학생은 합격입니다.")
