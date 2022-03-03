
# Prepare > Interview Preparation Kits > 1 Week Preparation Kit > Day 1 > Time Conversion
# https://www.hackerrank.com/challenges/one-week-preparation-kit-time-conversion/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    
    if s[-2:] == "AM":
        if s[:2] == "12":
            return "00" + s[2:8]
        return s[:8]
    else:
        if s[:2] == "12":
            return "12" + s[2:8]
        return str(int(s[0:2])+12) + s[2:8]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
