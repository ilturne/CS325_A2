import random
import time

def print_matrix():
    symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    width = 80
    height = 25
    matrix_year = 0
    print("Starting the Matrix...\n")

    while matrix_year != 10:
        matrix = [[random.choice(symbols) for _ in range(width)] for _ in range(height)]
        for row in matrix:
            print(''.join(row))
        time.sleep(0.1)
        matrix_year += 1 

    print("Uh oh, Neo escaped the matrix!")
