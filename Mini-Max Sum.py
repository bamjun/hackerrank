
# Prepare > Interview Preparation Kits > 1 Week Preparation Kit > Day 1 > Mini-Max Sum


# PrepareInterview Preparation Kits1 Week Preparation KitDay 1Mini-Max Sum


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    
    result_list = []
    
    sum_index = sum(arr)
    
    for x in arr:
        result_list.append(sum_index - x)
        
    print(min(result_list), end=" ")
    print(max(result_list))
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
