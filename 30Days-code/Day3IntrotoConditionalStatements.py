#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    if(N% 2==1):
        print('Weird')
    elif(N%2==0):
        if N in range(6,21):
            print("Weird")
        else:
            print('Not Weird')
        
