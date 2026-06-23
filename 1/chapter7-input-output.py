# 기본 입출력
# input() : 한 줄의 문자열을 입력 받는 함수
# map() : 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용
# 예시) 공백을 기준으로 구분된 데이터를 입력받을 때
# data = list(map(int, input().split()))
# print(data)
# 예시) 공백을 기준으로 구분된 데이터의 개수가 많지 않을 때
# a, b, c = list(map(int, input().split()))
# print("a: ", a)
# print("b: ", b)
# print("c: ", c)

print("-------------------------------")
# 데이터의 개수 입력
n = int(input())
print(n)
# 각 데이터를 공백을 기준으로 구분하여 입력
data = list(map(int, input().split()))
data.sort(reverse=True)
print(data)
# n, m, k 를 공백을 기준으로 구분하여 입력
n, m, k = map(int, input().split())
print(n, m, k)

# 빠르게 입력받기
# sys.stdin.readline() : 입력을 최대한 빠르게 받아야 하는 경우
# 입력 후 엔터가 줄바꿈 기호로 입력되므로 rstrip() 메서드를 함께 사용한다.
print("-------------------------------")
import sys

# 문자열 입력 받기
data = sys.stdin.readline().rstrip()
print(data)

# 자주 사용하는 표준 출력 방법
# print() : 기본적으로 이 함수를 쓴다.
# 각 변수를 콤마(,)를 이용하여 띄어쓰기로 구분하여 출력할 수 있다.
# 기본적으로 출력 이후 줄바꿈을 수행한다.
# 줄바꿈을 원치 않는 경우 'end' 속성을 이용한다.
print("-------------------------------")
# 출력할 변수들
a = 1
b = 2
print(a, b)
print(7, end=" ")
print(8, end=" /")
# 출력할 변수
answer = 7
print(" 정답은 " + str(answer) + "입니다.")

# f-string 예제
# 문자열 앞에 접두사 'f'를 붙여 사용한다.
# 중괄호 안에 변수명을 기입하여 간단히 문자열과 정수를 함께 넣을 수 있다.
answer1 = "정답"
answer2 = 9
print(f"정답은 {answer1}{answer2}입니다.")
