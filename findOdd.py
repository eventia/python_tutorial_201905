number = int(input("숫자를 넣으세요"))

if number > 0:

    if number % 3 == 0:
        print("3의 배수입니다.")

    if number % 2 == 0:
        print("짝수입니다.")

else :
    print("양의 정수를 입력하세요.")
