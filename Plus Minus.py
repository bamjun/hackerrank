Prepare > Interview Preparation Kits > 1 Week Preparation Kit > Day 1 > Plus Minus
https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positiveCount = 0;
    negativeCount = 0;
    zeroCount = 0;
 
    for i in range(n):
        if (arr[i] > 0):
            positiveCount += 1;
        elif(arr[i] < 0):
            negativeCount += 1;
        elif(arr[i] == 0):
            zeroCount += 1;
         
    print(round((positiveCount / n), 6));
    print(round((negativeCount / n), 6));
    print(round((zeroCount / n), 6));

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
