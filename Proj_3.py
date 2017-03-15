"""
Problem - 03
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

A = 600851475143 
B = 2

while (B<(A/2)):
    if A%B != 0:
        B = B+1

    else:
        A = A/B
        C= B
        B = 2
print (A)