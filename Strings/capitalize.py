# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 20:29:12 2023

@author: wwwta
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    if s.startswith(int):
        return s
    return s.title()
    s.capitalize()

if __name__ == '__main__':

    s = input()

    result = solve(s)

