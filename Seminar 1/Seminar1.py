number = int(input('Enter your number between 100 and 999: '))

if number > 99 and number <1000:
    def sum_of_digits(number):
        count = 0
        while number > 0:
            count = count + number % 10
            number //= 10
        return count

    print(sum_of_digits(number))
else:
    print('Your input is incorrect')