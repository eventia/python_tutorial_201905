print("{0:.4f}".format(1/3))
print("{0:.4f}".format(1/4))

print("{0}".format(2**80))
# 1208925819614629174706176
# 123,548,451
# 1.23 * 10^8
print("{0:.4g}".format(2**80))
# 1.209e+24

print("{0:_^11}".format("Hello"))
# ___Hello___

print("{name} wrote {book}".format(name="Baram", book="Zero Base Coding"))

print("Hello World", end="")
print("Hello World")  # end="\n"
print("Hello ")  # \n
# Hello WorldHello World
# Hello
"""
7 의  -2 승을 소수점이하 9번째 자리까지 출력하라
7 의 120 승을 유효숫자 9자리로 출력하라. (format 사용 g 옵션사용)
"""
print("{0}".format(7**-2))
print("{0:.9f}".format(7**-2))
print("{0}".format(7**120))
print("{0:.9g}".format(7**120))
# 0.02040816326530612
# 0.020408163
# 258086210989349276047917817413172383631691140276099547911280598425927853437317437263620645695945672001
# 2.58086211e+101
