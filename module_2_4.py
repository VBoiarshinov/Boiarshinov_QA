numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in range(len(numbers)):
    is_prime = True
    n = numbers[i]
    if n < 2:
        continue
    else:
        j = n ** 0.5
    for a in range(2, int(j + 1)):
        if n % a == 0:
            is_prime = False
            break
    if not (is_prime):
        not_primes.append(n)
    else:
        primes.append(n)
is_prime = True

print('Primes:', *primes)
print('Not Primes:', *not_primes)