
"""
Qual o laço mais rápido em Python?
04/08/2022
por Wesin Ribeiro
"""
import time
from statistics import mean


def debug_time(func, my_list):
    """Compute time ellapsed inside the loop"""
    times_list = []

    for _ in range(100):
        start_time = time.process_time()
        func(my_list)
        end_time = time.process_time()

        times_list.append(end_time - start_time)
    
    avg_time = mean(times_list)
    return f'{(avg_time * 1000):.2f} ms'


def for_loop(my_list):
    """Iterate over for loop."""
    for item in my_list:
        pass


def range_for_loop(my_list):
    """Iterate over range for loop."""
    for index in range(len(my_list)):
        pass

def enumerate_for_loop(my_list):
    """Iterate over enumerate for loop."""
    for index, item in enumerate(my_list):
        pass

def while_loop(my_list):
    """Iterate over while loop."""
    i = 0
    while i < len(my_list):
        i = i + 1
        pass

def range_for_loop_with_item(my_list):
    """Iterate over for loop unsing range with item access."""
    for index in range(len(my_list)):
        item = my_list[index]
        pass

def zip_for_loop(my_list):
    """Iterate over for loop using zip function."""
    for index, item in zip(range(len(my_list)), my_list):
        pass

def map_loop(my_list):
    """Iterate over map loop."""
    def loop(n):
        pass
    list(map(loop, my_list))

def main():
    """Show fastest loop in Python! Let's go!!!!"""
    length = 10000
    loop_list = [i for i in range(length)]
    loops = [
        {
            'method': 'for-loop',
            'index': 'no',
            'item': 'yes',
            'speed': debug_time(for_loop, loop_list)
        },
        {
            'method': 'range-loop',
            'index': 'yes',
            'item': 'no',
            'speed': debug_time(range_for_loop, loop_list)
        },
        {
            'method': 'enumerate_for-loop',
            'index': 'yes',
            'item': 'yes',
            'speed': debug_time(enumerate_for_loop, loop_list)
        },
        {
            'method': 'while-loop',
            'index': 'yes',
            'item': 'no',
            'speed': debug_time(while_loop, loop_list)
        },
        {
            'method': 'range for-loop item',
            'index': 'yes',
            'item': 'yes',
            'speed': debug_time(range_for_loop_with_item, loop_list)
        },
        {
            'method': 'zip for-loop',
            'index': 'yes',
            'item': 'yes',
            'speed': debug_time(zip_for_loop, loop_list)
        },
        {
            'method': 'map-loop',
            'index': 'no',
            'item': 'yes',
            'speed': debug_time(map_loop, loop_list)
        },
    ]
    print('\tMethod\t\tIndex\tItem\tSpeed')
    print('_'*23, '_'*6, '_'*6, '_'*8)
    for loop in loops:
        if len(loop['method']) > 14:
            end_method = '\t'
        else:
            end_method = '\t\t'
        print(loop['method'], end=end_method)
        print(loop['index'], end='\t')
        print(loop['item'], end='\t')
        print(loop['speed'])


main()