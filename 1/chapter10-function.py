# 함수 : 특정한 작업을 하나의 단위로 묶어놓은 것
# 내장 함수 : 파이썬이 기본적으로 제공하는 함수 (input, print 등)
# 사용자 정의 함수 : 개발자가 직접 정의하여 사용할 수 있는 함수.

# 매개변수 : 함수 내부에서 사용할 변수
# 반환 값 : 함수에서 처리된 결과를 반환
# 매개변수와 반환값은 존재하지 않을 수 있다.
# def 함수명(매개변수):


# 더하기 함수 예제
def add(a, b):
    return a + b


print(add(3, 7))

print("-------------------------------")


# 파라미터의 변수를 직접 지정할 수 있다.
def add(a, b):
    print("결과: ", a + b)


add(b=3, a=7)

print("-------------------------------")

# global 키워드 : 함수 바깥에 선언된 변수를 바로 참조하게 된다.
a = 0


def func():
    global a
    a += 1


for i in range(10):
    func()

print(a)

print("-------------------------------")


# 여러 개의 반환값
def operator(a, b):
    add_var = a + b
    subtract_var = a - b
    multiply_var = a * b
    divide_var = a / b
    return add_var, subtract_var, multiply_var, divide_var


a, b, c, d = operator(8, 4)
print(a, b, c, d)

print("-------------------------------")


# 람다 표현식 : 함수를 간단하게 작성할 수 있게 함. 함수 자체를 입력을 받는 함수가 있을 때 유용하다.
# 아래 두가지는 같은 것
# 일반적인 사용
def add(a, b):
    return a + b


print(add(3, 7))

# 람다 표현식으로 구현한 add() 메서드
print((lambda a, b: a + b)(3, 7))

print("-------------------------------")

# 내장 함수에서 자주 사용되는 람다 함수 예시
array = [("홍길동", 50), ("이순신", 32), ("아무개", 74)]


# 일반적인 함수
def my_key(x):
    return x[1]


print(sorted(array, key=my_key))
print(sorted(array, key=lambda x: x[1]))  # 람다 표현식 사용

print("-------------------------------")

# 여러 개의 리스트에 적용하는 예시
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
result = map(lambda a, b: a + b, list1, list2)
print(list(result))
