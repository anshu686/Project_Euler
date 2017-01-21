"""
Problem - 04
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
z = []
l =[]

for i in range(100, 1000):
    # print("i =", i, ":", end=" ")
    for j in range(100, 1000):
        p = i*j
        z.append(p)
    #     print("{:2d}".format(i * j), end=" ")
    # print()

def is_palindrome(i):
    s = str(i)
    if s == s[::-1]:
        return True
for digit in z:
    if (is_palindrome(digit)) == True:
        l.append(digit)
print(max(l))


