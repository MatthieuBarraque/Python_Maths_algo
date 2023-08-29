import sys
import math

def suite_geo(nb_initial_indiv, taux_croissance, nb_generations=None):
    if nb_generations is None:
        nb_generations = 100
    
    population = [(1, round(nb_initial_indiv, 2), 0) if int(nb_initial_indiv) == nb_initial_indiv else (1, round(nb_initial_indiv, 2))]

    for i in range(2, nb_generations+1):
        nb_indiv = taux_croissance * population[-1][1] * ((1000 - population[-1][1]) / 1000)
        if nb_indiv < 0:
            nb_indiv = 0
        generation = (i, round(nb_indiv, 2), 0) if int(nb_indiv) == nb_indiv else (i, round(nb_indiv, 2))
        population.append(generation)

    return population

if __name__ == '__main__':

    if len(sys.argv) == 2 and sys.argv[1] == "-h":
        print("USAGE\n")
        print("\t./106bombyx n [k | i0 i1]")
        print("DESCRIPTION\n")
        print("\tn\tnumber of first generation individuals")
        print("\tk\tgrowth rate from 1 to 4")
        print("\ti0\tinitial generation (included)")
        print("\ti1\tfinal generation (included)\n")
        exit(84)

    if len(sys.argv) == 3:
        if not all(char.isdigit() or char in ['.', '-'] for char in sys.argv[1]):
            exit(84)

        n = float(sys.argv[1])
        k = float(sys.argv[2])

        tab = suite_geo(n, k)
        for final in tab:
            print(*final)
            exit(0)