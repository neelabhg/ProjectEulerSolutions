# Problem 3 - Largest prime factor
#   The prime factors of 13195 are 5, 7, 13 and 29.
#   What is the largest prime factor of the number 600851475143 ?


def primes_sieve(limit):
    """
    Sieve of Eratosthenes - Generate the list of prime numbers upto limit
    Implementation taken from: http://stackoverflow.com/a/3941967/2193410
    """
    a = [True] * limit  # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):  # Mark factors non-prime
                a[n] = False


def trial_division(n):
    """
    Return a list of the prime factors for a natural number.
    Implementation taken from: http://en.wikipedia.org/wiki/Trial_division
    """
    if n == 1:
        return [1]
    primes = primes_sieve(int(n ** 0.5) + 1)
    prime_factors = []

    for p in primes:
        if p * p > n:
            break
        while n % p == 0:
            prime_factors.append(p)
            n /= p
    if n > 1:
        prime_factors.append(n)

    return prime_factors


def solution():
    return trial_division(600851475143)[-1]


if __name__ == '__main__':
    print solution()