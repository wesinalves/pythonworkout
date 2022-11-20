"""
Implementing Newton's method in Python
that is a way to quickly find a good approximation 
for the root of a real-valued function
---------------------------------------------------
100 days of pyhton code - 6/99
by Wesin Ribeiro
"""

import matplotlib.pyplot as plt

def f(x):
    return x**2 - 2

def f_prime(x):
    return 2*x

def newton_method(
    x0,         # the initial guess
    tolerance,  # accuracy
    epsilon,    # do not divide by a number smaller than this
    max_iterations
    ):
    guesses = []
    for i in range(max_iterations):
        y = f(x0)
        yprime = f_prime(x0)

        if abs(yprime) < epsilon:
            break

        x1 = x0 - y / yprime    # do Newton's computation

        if abs(x1 - x0) <= tolerance:
            guesses.append((x1, y))
            return x1, guesses
        
        guesses.append((x1, y))

        x0 = x1
    
    return None

def main():
    X = [x for x in range(-18, 20)]
    Y = [f(x) for x in X]

    root, guesses = newton_method(15, 0.0001, 0.00001, 50)
    print(root)

    # let's plot the graph
    plt.plot(X, Y, 'r-', label='function')
    plt.plot([g[0] for g in guesses], [g[1] for g in guesses], 'bo', label='guesses')
    plt.grid()
    plt.legend()
    plt.show()

main()
