'''
Heap sort algorithm
by Wesin Ribeiro
100 days of code in Python
12/99
'''

from random import shuffle

def max_heapfy(elements, length, index):
    '''Make sure max heap property.'''
    current_parent = index
    child_left = index * 2 + 1
    child_right = index * 2 + 2

    if child_left <= length and elements[child_left] > elements[current_parent]:
        current_parent = child_left

    if child_right <= length and elements[child_right] > elements[current_parent]:
        current_parent = child_right
    
    if current_parent != index:
        elements[index], elements[current_parent] = elements[current_parent], elements[index]
        max_heapfy(elements, length, current_parent)

def build_max_heap(elements):
    '''Build a max heap.'''
    length = len(elements)
    for i in range(length // 2 - 1, -1, -1):
        max_heapfy(elements, length -1, i)

def heap_sort(elements):
    '''Sort elements in ascending order.'''
    length = len(elements)
    build_max_heap(elements)
    for i in range(length - 1, 0, -1):
        elements[i], elements[0] = elements[0], elements[i]
        max_heapfy(elements, i - 1, 0)

def main():
    '''Run main funcion.'''
    scores = list(range(100))
    shuffle(scores)

    print(scores)
    heap_sort(scores)
    print(scores)

main()