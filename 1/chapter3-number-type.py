# 1.1 정수형

# 양의 정수
a = 1000
print(a)
# 음의 정수
a = -1
print(a)
# 0
a = 0
print(a)
# 덧셈 / 뺄셈
a = a + 5
print(a)
a = a - 3
print(a)


# 1.2 실수형

# 양의 실수
a = 156.23
print(a)
# 음의 실수
a = -141.5
print(a)
# 소수부가 0일 때는 0 생략 가능 (자동 포맷으로 적용돼서 지금은 들어가있음)
a = -5.0
print(a)
# 정수부가 0일 때 0 생략 가능
a = -0.5
print(a)


# 1.3 지수 표현 방식 (기본적으로 실수로 출력. 무한이라는 의미를 가진 값을 임의의 큰 수를 설정할 때 사용하기도 함)

# 1,000,000,000 의 지수 표현 방식
a = 1e9
print(a)
# 725.5
a = 75.25e1
print(a)
# 3.954
a = 3954e-3
print(a)
# 정수로 바꾸기
a = int(1e9)
print(a)
# 실수 정보를 표현하는 정확도에 한계를 가짐. 0.3과 0.6을 더한 값이 정확히 0.9가 되지 않는다.
a = 0.3 + 0.6
print(a)
if a == 0.9:
    print(True)
else:
    print(False)
# round() 함수를 반올림 목적으로 사용하여 해결한다.
a = 0.3 + 0.6
print(round(a, 4))
if round(a, 4) == 0.9:
    print(True)
else:
    print(False)
# 수 자료형의 연산
a = 7
b = 3
# 나누기
print(a / b)
# 나머지
print(a % b)
# 몫
print(a // b)
# 거듭 제곱
print(a**b)
# 제곱근
print(a**0.5)
