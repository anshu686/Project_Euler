"""
Problem - 04
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
a=[]
b=[]
for i in range(100,1000):
    for j in range(100,1000):
        x = i*j
        a.append(x)
for y in a:
    z = str(y)
    if z == z[::-1]:
        b.append(y)
print (max(b))


