n = 385916

sum1 = 0
sum2 = 0

while n > 0:
    if n > 1000:
        a = n % 10
        sum2 = sum2 + a
        n = n // 10
    else:
        a = n % 10
        sum1 = sum1 + a
        n = n // 10

if sum1 == sum2:
    print('yes')
else:
    print('no')