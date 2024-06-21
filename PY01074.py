def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return factors

def sum_of_prime_factors(numbers):
    total_sum = 0
    for num in numbers:
        factors = prime_factors(num)
        total_sum += sum(factors)
    return total_sum
n = int(input())
numbers = [int(input()) for _ in range(n)]
result = sum_of_prime_factors(numbers)
print(result)
