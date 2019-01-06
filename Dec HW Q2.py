num = 1
tnum = 0
prod = 1
n = 0

while num != 0:
    num = int(input("Enter Number, '0' to stop: "))
    if num != 0:
        prod = prod * num
        tnum = tnum + num
        n = n + 1

avg = tnum / n
print ("Average:", avg, "    Product:", prod)
