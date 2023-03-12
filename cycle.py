# арифметическая прогрессия:
a = int(input('первый член: '))
b = int(input('разность: '))
c = int(input('номер последнего члена: '))
sum = 0
for i in range(a, a + b*c, b):
    sum += i
print('сумма арифметической прогрессии: ', sum)

# ----------------------------------------------------

a = int(input('первый член: '))
b = int(input('разность: '))
c = int(input('номер последнего члена: '))
sum = (c/2) * (2*a + (c-1)*b)
print('сумма арифметической прогрессии: ', sum)

# ----------------------------------------------------

# геометрическая прогрессия:
a = int(input('первый член: '))
b = int(input('знаменатель: '))
c = int(input('номер последнего члена: '))
sum = 0
for i in range(c):
    sum += a * b**i
print('cумма геометрической прогрессии: ', sum)

# ----------------------------------------------------

a = int(input('первый член: '))
b = int(input('знаменатель: '))
c = int(input('номер последнего члена: '))
sum = a * (1 - b**c) / (1 - b)
print('сумма геометрической прогрессии:', sum)

# ----------------------------------------------------

 def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return True
    return False
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 5
if binary_search(arr, x):
    print('значение найдено')
else:
    print('значение не найдено')

# ----------------------------------------------------

def coin_change(amount, coins):
    coins.sort(reverse=True)
    coin_count = [0] * len(coins)
    for i, coin in enumerate(coins):
        coin_count[i] = amount // coin
        amount = amount % coin
    return coin_count
coins = [1, 2, 5, 10, 20, 50, 100]
amount = int(input('сумма: '))
coin_count = coin_change(amount, coins)

print('количество купюр/монет номиналом:')
for i, coin in enumerate(coins):
    print("{} - {}".format(coin, coin_count[i]))