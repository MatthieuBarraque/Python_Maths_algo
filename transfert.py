import sys

def display_help():
    print("USAGE:")
    print("./107transfer [num den]+")
    print("DESCRIPTION")
    print("num polynomial numerator defined by its coefficients")
    print("den polynomial denominator defined by its coefficients")

def parse_polynomial(poly_str):
    try:
        return [int(c) for c in poly_str.split("*")]
    except ValueError:
        print(f"Invalid polynomial: {poly_str}")
        sys.exit(84)

def evaluate_polynomial(poly, x):
    return sum([c * x**i for i, c in enumerate(poly)])

def evaluate_transfer_function(num_poly, den_poly, x):
    num = evaluate_polynomial(num_poly, x)
    den = evaluate_polynomial(den_poly, x)
    return num / den

def main():
    if len(sys.argv) == 2 and sys.argv[1] == "-h":
        display_help()
        sys.exit(0)
    elif len(sys.argv) != 3:
        print("Invalid number of arguments")
        sys.exit(84)

    num_poly = parse_polynomial(sys.argv[1])
    den_poly = parse_polynomial(sys.argv[2])

    for i in range(1001):
        x = i / 1000
        response = evaluate_transfer_function(num_poly, den_poly, x)
        print("{:.3f} -> {:.5f}".format(x, response))

if __name__ == "__main__":
    main()