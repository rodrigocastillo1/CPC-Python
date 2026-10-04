import numpy as np
import sys

def task1_1():
    # Create a vector with values ranging from 10 to 49.
    # Reverse a vector (first element becomes last)
    v = np.arange(10, 50)
    print("Vector with values 10 to 49: ", v)
    print("Reversed vector: ", v[::-1])
    return

def task1_2():
    # Consider a generator function that generates 10 integers and use it
    # to build an array
    a = np.linspace(1, 10, 10).astype(np.int_)
    print("Array of", a.size, "integers generated with np.linspace:", a)
    return

def task2_1():
    # Create a 5x5 array with random values and find the minimum and maximum values
    m = np.random.random((5,5))
    print("5x5 matrix of random values:\n", m)
    print("Maximum value: ", m.max(), ". Minimum value: ", m.min())
    return

def task2_2():
    # Consider two random array A and B, check if they are equal
    arrayA = np.random.random(3)
    arrayB = np.random.random(3)
    print("Array A:\n", arrayA)
    print("Array B:\n", arrayB)
    print("Are arrays equal? -> ", np.array_equal(arrayA, arrayB))
    return

def task3_1():
    # Normalize a 5x5 random matrix
    nm = np.random.uniform(0, 1, (5, 5))
    print("Normalized matrix with values between 0 and 1:\n", nm)
    return

def task3_2():
    # Consider a random vector with shape (100,2) representing coordinates,
    # find point by point distances
    coords = np.random.random((100, 2))
    dist = np.empty((0,100), float)

    for point in coords:
        dist = np.append(dist, [np.sqrt(np.sum((coords - point)**2, axis=1))], axis=0)

    print("Coordinates array:\n", coords)
    print("Distances matrix:\n", dist)
    return

def task4_1():
    # Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)
    matrix5_3 = np.random.randint(10, size=(5, 3))
    matrix3_2 = np.random.randint(10, size=(3, 2))
    matrix5_2 = np.dot(matrix5_3, matrix3_2)

    print("Matrix 5x3:\n", matrix5_3)
    print("Matrix 3x2:\n", matrix3_2)
    print("Multiplicated:\n", matrix5_2)
    return

def task4_2():
    # Subtract the mean of each row of a matrix
    m = np.random.random((3, 3))
    mean = np.array([np.apply_along_axis(np.mean, axis=1, arr=m)]).T
    print("Original matrix:\n", m)
    print("Row Mean vector:\n", mean)
    print("Substract mean of each row:\n", m-mean)
    return

def task5_1():
    # How to get the dates of yesterday, today and tomorrow?
    today = np.datetime64('today', 'D')
    yesterday = today - np.timedelta64(1, 'D')
    tomorrow = today + np.timedelta64(1, 'D')
    print("Yesterday:", yesterday)
    print("Today:", today)
    print("Tomorrow:", tomorrow)
    return

def task5_2():
    # How do I sort an array by the nth column?
    nth_column = np.random.randint(0, 4, 1)[0]
    print(nth_column)
    a = np.random.randint(0, 9, (4,4))
    print("Original array:\n", a)
    sa = a[a[:,nth_column].argsort()]
    print("Sorted array by column", nth_column, "\n", sa)
    return

def task6_1():
    # Extract the integer part of a random array using 5 different methods
    arr = np.random.uniform(0, 10, 3)
    print("Original array:\n", arr)
    
    print("1st method. np.floor:", np.floor(arr))
    print("2nd method. np.trunc:", np.trunc(arr))
    print("3rd method. arr.astype:", arr.astype(int))
    print("4th method. arr // 1: ", arr // 1)
    arr = np.array([int(n) for n in arr])
    print("5th method. compression list: ", arr)
    return

def task6_2():
    # Compute a matrix rank
    matrix = np.random.randint(0, 10, (3,4))
    rank = np.linalg.matrix_rank(matrix)
    print("1. Matrix with rank", rank, ":\n", matrix)
    matrix = np.array([[2, 4, 6], [4, 8, 12], [0, 1, 2]])
    rank = np.linalg.matrix_rank(matrix)
    print("2. Matrix with rank", rank, ":\n", matrix)
    return

def task7_1():
    # Create a structured array representing a position (x,y) and
    # a color (r,g,b)
    matrix_dtype = [('position', [('x', float), ('y', float)]),
                    ('color', [('r', np.uint8), ('g', np.uint8), ('b', np.uint8)])]
    im = np.array([((0, 1), (5, 245, 126)),
                   ((0, 2), (110, 211, 18)),
                   ((0, 3), (45, 145, 200))],
                   dtype=matrix_dtype)

    print("Position and Colors:\n", im)
    x_pos = 0
    y_pos = 1
    mask = (im['position']['x'] == x_pos) & (im['position']['y'] == y_pos)
    print("Color at (", x_pos, ",", y_pos, "): ", im['color'][mask])
    return

def task7_2():
    # Consider a 16x16 array, how to get the block-sum (block size is 4x4)
    m = np.random.randint(0, 10, (16,16))
    print("16x16 matrix:\n", m)
    nm = m.reshape(4, 4, 4, 4)
    block_sum = nm.sum(axis=(1,3))
    print("Block Sum (4x4 matrix):\n", block_sum)
    return


def main():
    print("This program will execute the tasks of the Numpy module of CPC course.")
    #tasks = [task7_2]
    tasks = [task1_1, task1_2, task2_1, task2_2, task3_1, task3_2,
             task4_1, task4_2, task5_1, task5_2, task6_1, task6_2,
             task7_1, task7_2]

    for t in tasks:
        print("\n-------------------------------------------------\n")
        print("-> Executing", t.__name__,":")
        t()

if __name__ == "__main__":
    main()