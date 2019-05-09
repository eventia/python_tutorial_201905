import sys

t1 = sys.maxsize
t2 = t1+1  #파이썬 3.x 에서는 long, int 통합
t3 = t2**10  # 큰 수도 O.K.
print(t1)
print(t2)
print(t3)
print(type(t1))
print(type(t2))
print(type(t3))

age = 26
name = '(Python'

print('{0} was {1} years old'.format(name, age))
print('{0} is easy'.format(name))
