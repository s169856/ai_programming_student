"""
Oefening 1: Insertion Sort
===========================
Implementeer insertion sort volgens het stappenplan in opgave_week1.md.
"""

from time import time
import random


def timer_func(suppress_output=False):
    # dit geeft aan hoelang de functie die het meekrijgt heeft gerund
    def actual_decorator(func):
        def wrap_func(*args, **kwargs):
            t1 = time()
            result = func(*args, **kwargs)
            t2 = time()
            if not suppress_output:
                print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
            return result, t2-t1
        return wrap_func
    return actual_decorator


def insertion_sort(sequence):
    """
    Sorteer een lijst van klein naar groot met behulp van insertion sort.

    Parameters:
        sequence (list): De lijst om te sorteren.

    Returns:
        list: De gesorteerde lijst.
    """
    # TODO: implementeer insertion sort
    startIndex = 1

    while startIndex < len(sequence):
        key = sequence[startIndex]
        i = startIndex

        while i >= 0:
            if i > 0 and key < sequence[i-1]:
                sequence[i] = sequence[i-1]
            else:
                sequence[i] = key
                break
            i-= 1

        startIndex += 1

    return sequence

@timer_func(suppress_output=True) #decorator gebruiken
def bubble_sort(sequence):
    n = len(sequence)
    for i in range(n-1):
        for j in range(n-i-1):
            if(sequence[j] > sequence[j+1]):
                sequence[j], sequence[j+1] = sequence[j+1], sequence[j] # wisselen van plaats

@timer_func(suppress_output=True) #decorator gebruiken
def merge_sort(sequence):
    size = len(sequence)
    if size > 1:
        middle = size // 2
        left_arr = sequence[:middle]
        right_arr = sequence[middle:]
 
        merge_sort(left_arr)
        merge_sort(right_arr)
 
        p = 0
        q = 0
        r = 0
 
        left_size = len(left_arr)
        right_size = len(right_arr)
        while p < left_size and q < right_size:
            if left_arr[p] < right_arr[q]:
              sequence[r] = left_arr[p]
              p += 1
            else:
                sequence[r] = right_arr[q]
                q += 1
             
            r += 1
 
        
        while p < left_size:
            sequence[r] = left_arr[p]
            p += 1
            r += 1
 
        while q < right_size:
            sequence[r]=right_arr[q]
            q += 1
            r += 1

if __name__ == "__main__":
    # Test je implementatie met deze voorbeelden
    test_lijsten = [
        [],
        [42],
        [1, 2, 3, 4],
        [5, 4, 3, 2, 1],
        [3, 1, 2, 1, 3],
        [5, 2, 4, 6, 1, 3],
    ]

    for lijst in test_lijsten:
        origineel = lijst.copy()
        gesorteerd = insertion_sort(lijst)
        print(f"Origineel: {origineel} -> Gesorteerd: {gesorteerd}")

    # Stap 5 (uitbreiding): vergelijk met bubble sort en merge sort
    # Kopieer bubble_sort en merge_sort uit de cursus en test hier:
    # import random
    # import time
    # ...

    n = 4000 #max 5000
    r = 100 #repitions
    average_bubble = 0
    
    for i in range(0,r):
        sequence = random.sample(range(n), n)
        result = bubble_sort(sequence)
        average_bubble += result[1] / r
    print("Average time to complete: " + f'{(average_bubble):.4f}s')
