n = int(input('Chocolat n-size: '))
m = int(input('Chocolat m-size: '))
k = int(input('Chocolat k-pics: '))

if k < n * m and (k % n == 0) or (k % m == 0):
    print('YES! You may slice your chocolat!')
else:
    print('NO! You can not slice your chokolat')