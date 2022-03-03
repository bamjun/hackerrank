# Prepare > Interview Preparation Kits > 1 Week Preparation Kit > Day 2 > Diagonal Difference
# https://www.hackerrank.com/challenges/one-week-preparation-kit-diagonal-difference/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-two&h_r=next-challenge&h_v=zen

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    first_x_index = []
    second_x_index = []
    
    for x in range(n):
        first_x_index.append(arr[x][x])
    
    y = 0
    for x in range(n-1, -1, -1):
        second_x_index.append(arr[y][x])
        y = y+1
        
    a = sum(first_x_index)
    b = sum(second_x_index)
    
    return abs(a - b)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
