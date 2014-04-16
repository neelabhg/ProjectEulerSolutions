# Problem 4 - Largest palindrome product
#   A palindromic number reads the same both ways.
#   The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
#   Find the largest palindrome made from the product of two 3-digit numbers.


def is_palindromic(n):
    s = str(n)
    for i in xrange(len(s) / 2):
        if s[i] != s[-(i+1)]:
            return False
    return True


def solution():
    max_palindrome = 0
    for i in xrange(999, 99, -1):
        for j in xrange(999, 99, -1):
            p = i * j
            if p > max_palindrome and is_palindromic(p):
                max_palindrome = p
    return max_palindrome


if __name__ == '__main__':
    print solution()