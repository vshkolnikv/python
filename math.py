a = 5
b = 10
ex1 = (a - b) * (a + b)
print(ex1)
ex2 = a**2 - 2*a*b + b**2
print(ex2)
ex3 = a**2 + 2*a*b + b**2
print(ex3)
ex4 = a**3 - 3*a**2*b + 3*a*b**2 - b**3
print(ex4)
ex5 = a**3 + 3*a**2*b + 3*a*b**2 - b**3
print(ex5)
ex6 = (a + b)*(a**2 + a*b + b**2)
print(ex6)
ex7 = (a - b)*(a**2 + a*b + b**2)
print(ex7)

# --------------------

a = 5
b = 10
c = 15
ex = ((((a * a) + ((a + c)**2) / (10 * b))- (c**2 * a * 4))**(-1/2))
print(ex)

# --------------------

p = []
d = 0
sum = int(input())
print('sum', sum)
for i in range(sum):
    p.append(float(input(p)))
    print('p', p)
for i in range(len(p)):
    d += p[i]*math.log(p[i], 2)
    print('d', d)
print(-(round(d, 3)))

# --------------------

number = 0.1
while number <= 0.3:
    number += 0.1
    print(number)
number = round(number, 1)
print(number)