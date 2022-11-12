from random import randint

def bubble_sort(vector):
    '''sort a vector in ascending order'''
    length = len(vector)

    for i in range(length):
        for j in range(length - i - 1):
            if vector[j] > vector[j+1]:
                vector[j], vector[j+1] = vector[j+1], vector[j]

def main():
    '''Main function'''
    elements = [randint(0,100) for _ in range(10)]
    print(elements)
    bubble_sort(elements)
    print(elements)

main()