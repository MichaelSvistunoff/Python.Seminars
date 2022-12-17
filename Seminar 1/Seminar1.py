number = int(input('Enter your number: '))

if number > 99999 and number < 1000000:
    sum_one = 0
    sum_two = 0

    for i in range(6):
        if i < 3:
            sum_one = sum_one + number // 10 ** i % 10
        else:
            sum_two = sum_two + number // 10 ** i % 10
    if sum_one == sum_two:
        print('YES! Your ticket is lucky!')
    else:
        print('Your ticket is not lucky...')
else:
    print("You've inputed incorrect number!")