import csv
import numpy as np

def help():
    print("USAGE")
    print("\t./109titration file\n")
    print("DESCRIPTION")
    print("\tfile\tcsv file containing \"vol;ph\" lines")

def read_csv(filename):
    data = []
    with open(filename) as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            data.append([float(row[0]), float(row[1])])
    return np.array(data)

def derivative(x, y):
    dx = x[1:] - x[:-1]
    dy = y[1:] - y[:-1]
    return dy / dx

def main(filename):

    if len(sys.argv) != 2:
        print("Usage : ./109titration file.csv (-h for help)")
        sys.exit(1)
    
    elif len(sys.argv) == 2 and sys.argv[1] == "-h":
        help()
    
    else:
        data = read_csv(filename)
        x = data[:, 0]
        y = data[:, 1]
        d1 = derivative(x, y)
        print("Derivative:")
        for i in range(len(x) - 1):
            print("%.1f ml -> %.2f" % (x[i], d1[i]))

if __name__ == '__main__':
    import sys
    main(sys.argv[1])