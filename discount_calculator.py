n = int(input("Enter bill amount: "))
even = 0
odd = 0

while n != 0:
    r = n % 10
    if r % 2 == 0:
        even += r
    else:
        odd += r
    n = n // 10

discount = even * odd
print("Discount:", discount)
