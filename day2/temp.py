#reusable fntn to create temp
def temp(celsius):
    fahrenheit=(99/5)*celsius+32
    return fahrenheit
t=float(input("Enter the temperature in celsius:"))
print("fahrenheit is:",temp(t))