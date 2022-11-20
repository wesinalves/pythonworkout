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
    """Dlecare function to find the root."""
    return x**2 - 2   # f(x) = x^2 - 2

def f_prime(x):
    """Dlecare derivative of the function to find the root."""
    return 2*x        # f'(x) = 2x

def newtons_method(
    x0,               # The initial guess    
    tolerance,        # 7-digit accuracy is desired
    epsilon,          # Do not divide by a number smaller than this
    max_iterations,   # The maximum number of iterations to execute
    ):
    guesses = []
    for i in range(max_iterations):
        y = f(x0)
        yprime = f_prime(x0)

        if abs(yprime) < epsilon:       
            break

        x1 = x0 - y / yprime        # Do Newton's computation

        if abs(x1 - x0) <= tolerance:   
            guesses.append((x1, y))
            return x1, guesses          
        
        guesses.append((x1, y))
        x0 = x1                         

    return None  

def main():
    x = [i for i in range(-18, 20)]
    y = [f(e) for e in x]

    root, guesses = newtons_method(14, 0.0001, 0.00001, 50)
    print(root)

    plt.plot(x,y, 'r-')
    plt.plot([g[0] for g in guesses],[g[1] for g in guesses], 'bo')
    plt.grid()
    plt.show()

main()