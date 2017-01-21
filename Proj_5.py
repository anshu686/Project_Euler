"""
Problem - 05
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""
n = 1
for k in range(1, 21):
    if n % k > 0:
        for j in range(1, 21):
            if (n*j) % k == 0:
                n *= j
                break
print (n)