j = 2
print(j)    # 2

j = j
print(j)    # 2

j = 2j      # 0+2j
print(j)    # 2j

j = 2*j
print(j)    # 4j

a = 1-2j
b = complex(1,2)  # 1+2j

print(a+b)  # 2  ... (2+0j)
print(a-b)  # -4j
print(a*b)  # (1-2j)(1+2j) = 1 + 4 = 5 ... (5+0j)
print(a/b)
"""
a.real		# 실수부
a.imag		# 허수부
a.conjugate() 	# 켤레복소수
abs(a)		# 크기
"""
print(a.real)  # 1.0
print(a.imag)  # -2.0
print(a.conjugate())  # (1+2j)
print(abs(a))  # 2.23606797749979
