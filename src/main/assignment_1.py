import math
import numpy as numpy
from scipy.misc import derivative
import sympy as smp

def approximation_algorithm(x0):
    i = 0
    diff = x0
    x = x0
    tol = 1e-6

    print("\nstart approximation algorithm")

    print(str(i) + ' : ' + str(x))

    while(diff>=tol): 
        i += 1
        y = x
        x = (x/2) + (1/x)

        print(str(i) + " : " + str(x))
        diff = abs(x-y)
    print("Convergence after " + str(i) + " iterations")
    print("end approximation algorithm\n")

    return

def bisection_method(f, a, b, max, tol=1e-6):
    i = 0
    p = 0

    print("\nstart bisection algorithm")

    while((abs(b - a) > tol) & (i < max)):
        i += 1
        p = (a+b)/2

        if((f(a)<0) & (f(p)>0) | (f(a)>0) & (f(p)<0)):
            b = p
        else:
            a = p
    print("output: " + str(p) + " after " + str(i) + " iterations")
    print("end bisection algorithm\n")
    return


def fixed_point_iteration(g, approx, N, tol=1e-6):
    i = 1

    print("\nstart Fixed Point Iteration algorithm")

    while(i <= N):
        p = g(approx)
        print(str(i) + " : " + str(p))
        if (abs(p-approx) < tol):
            print("success")
            break
        i += 1
        approx = p

    print("end Fixed Point Iteration algorithm\n")
    return

def newton_raphson_method(h, approx, N, tol=1e-6):
    i = 1
    print("\nstart Newton Raphson Method algorithm")

    while(i <= N):
        if(derivative(h, approx, dx=1e-6) != 0):
            p = approx - h(approx)/derivative(h, approx, dx=1e-6)
            if(abs(p-approx)<tol):
                print("done: " + str(p))
                print("end Newton Raphson Method algorithm\n")
                return
            i += 1
            approx = p
        else:
            print("failure: derivative is zero")
    print("failure: max iterations")

    print("end Newton Raphson Method algorithm\n")
    return

if __name__ == "__main__":
    # Example usage
    x_value = 1.5
    maximum = 100
    f = lambda x: x - x**3 - 4 * x**2 + 10
    g = lambda x: x - (1/x) + 1/math.tan(x)
    h = lambda x: math.cos(x)
    a = 1
    b = 2
    approx = 4
    approx2 = math.pi/4

    approximation_algorithm(x_value)

    bisection_method(f, a, b, maximum)

    fixed_point_iteration(g, approx, maximum)

    newton_raphson_method(h, approx2, maximum)
