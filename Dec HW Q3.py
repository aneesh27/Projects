for num in range (100, 501):
    dig3 = num % 10
    num2 = num - dig3
    num2 = num2 / 10
    dig2 = num2 % 10
    dig1 = num2 - dig2
    dig1 = dig1 / 10

    dig1 = dig1 ** 3
    dig2 = dig2 ** 3
    dig3 = dig3 ** 3

    tdig = dig1 + dig2 + dig3
    if tdig == num:
        print(num)
