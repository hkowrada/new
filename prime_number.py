num = int(input('enter a number'))
if num == 0:
    print(''' '0'(Zero can never be a prime number as it can be divided by 1, and any other number.
          It has an infinite number of divisors and therefore doesn't meet the definition.)''')
elif num == 1:
    print(''' A number divisible by only 2 (different) numbers; being
                            1; and
                            The number itself.
             Following that definition we can see that 1 is divisible by 1, and itself. But the 2 numbers are the same.
             So it is not a prime.''')
elif num == 2:
    print('2 is a even prime number')
else:
    for i in range(2, num):
        if num % i == 0:
            print(num, 'Number is not Prime')
            exit()
    else:
        print(num, 'Number is PRIME')
