aNum = int(input("시작하는 수를 입력하세요 : "))
zNum = int(input("끝나는 수를 입력하세요 : "))


for anyNum in range(aNum,zNum+1):
    isPrime = 0
    if anyNum == 2 or anyNum == 3 or anyNum == 5 or anyNum == 7:
        isPrime = 0
    elif anyNum == 1:
        isPrime = 1
    elif anyNum % 2 == 0:
        isPrime = 1
    elif anyNum % 3 == 0:
        isPrime = 1
    else :

        for countNum in range(1,anyNum//12):
            if anyNum % (6*countNum+1) == 0:
                isPrime = 1
                break
            if anyNum % (6*countNum-1) == 0:
                isPrime = 1
                break

    if isPrime == 0:
        print(anyNum)
