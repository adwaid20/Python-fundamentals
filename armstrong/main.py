num = int(input("Enter a number: "))
temp = num  # store original number
n = len(str(num))  # count digits
total = 0

while temp > 0:
    digit = temp % 10          # get last digit
    total += digit ** n        # add digit^n
    temp //= 10                # remove last digit

if total == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

















