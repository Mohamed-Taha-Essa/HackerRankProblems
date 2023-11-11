'''
Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements,
and swaps them if they are in the wrong order. The pass through the list is repeated until the list
 is sorted. Here's an example implementation of Bubble Sort in Python

'''
if False:
    count =0
    def bubble_sort(arr):
        n = len(arr)
        # Traverse through all elements in the list
        
        for i in range(n):
            global count 
            # Last i elements are already in place, so we don't need to check them
            for j in range(0, n-i-1):
                # Swap if the element found is greater than the next element
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    count +=1

    # Example usage
    my_list = [64, 34, 25, 12, 22, 11, 90]
    a =[3,2,1]
    bubble_sort(a)

    print("Sorted array:", a)
    print(f"Array is sorted in {count} swaps")
    print("First Element:",a[0])
    print("Last Element:" ,a[-1])

    print(count)


#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    n = len(arr)
    # Traverse through all elements in the list
    count=0 
    for i in range(n):
        
        # Last i elements are already in place, so we don't need to    check them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element      
              
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                count +=1

    # Write your code here
    
    print(f"Array is sorted in {count} swaps.")
    print("First Element:",arr[0])
    print("Last Element:" ,arr[-1])
