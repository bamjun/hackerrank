
# Prepare > Interview Preparation Kits > 1 Week Preparation Kit > Day 2 > Lonely Integer
# https://www.hackerrank.com/challenges/one-week-preparation-kit-lonely-integer/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-two


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    a.sort()
    second_index = a[0]

    if n == 1:
        return a[0]

    confirm_index = 0

    for x in range(n):
        first_index = a[x]
        if first_index != second_index:
            if confirm_index != 1:
                return second_index
            confirm_index = 0
            second_index = first_index
        else:
            confirm_index = 1
            second_index = first_index

    return a[-1]
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
