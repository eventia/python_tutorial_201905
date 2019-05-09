aNum = int(input("시작하는 수를 입력하세요 : "))
zNum = int(input("끝나는 수를 입력하세요 : "))

for anyNum in range(aNum,zNum+1):
    isPrime = 0

    for countNum in range(2,anyNum):
        if anyNum % countNum == 0:
            isPrime = isPrime + 1

    if isPrime == 0:
        print(anyNum)
