from math import sin, asin, pi, degrees, radians,cos

# n = 1.2
# for i in range(90):
#     j = degrees( asin( sin(radians(i)) * n ) )
#     print(i,j,j-i)
print(310*sin(radians(77)))


# ns = [1.2, 4/3, 1.4, 2.0]
# for n in ns:
#     j = degrees(asin(1/n))
#     print(j, n)

# List = [1516, 500, 760, 14560, 2560, 1960, 3480, 4980, 2220, 4240, 760, 1120]
# print(len(List), sum(List))
# tmp = 0
# for i in List:
#     print(i*1.1)
#     tmp += i*1.1
# print(tmp, sum(List)*1.1)

p = [0.1, 0.09, 0.081, 0.0729, 0.06561, 0.059049, 0.0531441, 0.4782969]
# l = [3,4,4,4,4,4,4,1]
# l = [3,3,3,3,3,4,4,2]
l = [3,5,5,5,5,3,3,1]
n = [1,2,3,4,5,6,7,7]
a = 0
for i,j,k in zip(p,l,n):
    a += i*j/k
print(a)