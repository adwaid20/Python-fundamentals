squares = [x**2 for x in range(1, 11)]
print(squares)  

primes = [num for num in range(2, 51)
          if all(num % i != 0 for i in range(2, num))]
print(primes)