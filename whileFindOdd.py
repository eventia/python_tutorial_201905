
number = 0

while (number != 777):
    number = int(input("숫자를 넣으세요 : "))
    if number % 3 == 0:
        print("3의 배수입니다.")

    if number % 2 == 0:
        print("짝수입니다.")

    if number == 777:
        print("프로그램을 종료합니다.")
