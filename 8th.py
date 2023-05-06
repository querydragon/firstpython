# % 연산자: % 연산자는 나머지(Modulus) 연산을 수행합니다. num1 % num2는 num1을 num2로 나눈 나머지를 반환합니다. 예를 들어, 7 % 3은 1을 반환합니다.
# ** 연산자: ** 연산자는 거듭제곱(Power) 연산을 수행합니다. num1 ** num2는 num1을 num2번 곱한 값을 반환합니다. 예를 들어, 2 ** 3은 8을 반환합니다.

num1 = int(input("숫자1 ====>"))
num2 = int(input("숫자2 ====>"))
result1 = num1 + num2
result2 = num1 - num2
result3 = num1 * num2
result4 = num1 / num2
result5 = num1 % num2
result6 = num1 ** num2
print(num1, "+", num2, "=", result1)
print(num1, "-", num2, "=", result2)
print(num1, "*", num2, "=", result3)
print(num1, "/", num2, "=", result4)
print(num1, "%", num2, "=", result5)
print(num1, "**", num2, "=", result6)