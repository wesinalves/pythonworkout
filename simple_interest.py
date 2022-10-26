"""
Python program to find simple interest
for given principal amount, time and
rate interest

si = (a * t * r)/100
"""


def simple_interest(a, t, r):
    """Compute simple interest."""
    print("The amount is", a)
    print("The time period is", t)
    print("The rate of interest is", r)

    si = (a * t * r)/100

    print("The Simple Interest is", si)

    fa = a + si
    print("The final amount is", fa)
    return fa


if __name__ == "__main__":
    simple_interest(8, 5, 3)