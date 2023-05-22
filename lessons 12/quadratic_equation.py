import argparse
import math


def solve_quadratic_equation(a, b, c):
    """Solves a quadratic equation and returns the roots"""
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None
    elif discriminant == 0:
        x = -b / (2*a)
        return x, x
    else:
        sqrt_discriminant = math.sqrt(discriminant)
        x1 = (-b + sqrt_discriminant) / (2*a)
        x2 = (-b - sqrt_discriminant) / (2*a)
        return x1, x2


def main():
    parser = argparse.ArgumentParser(description='Calculation of the quadratic equation')
    parser.add_argument('-a', type=float, default=0, help='parameter a')
    parser.add_argument('-b', type=float, required=True, help='parameter b')
    parser.add_argument('-c', type=float, required=True, help='parameter c')

    args = parser.parse_args()
    a = args.a
    b = args.b
    c = args.c

    if a == 0:
        print("Error: parameter a cannot be 0")
        return

    roots = solve_quadratic_equation(a, b, c)
    if roots is None:
        print("The equation has no real roots")
    else:
        print("Root equations:")
        for root in roots:
            print(root)


if __name__ == '__main__':
    main()
