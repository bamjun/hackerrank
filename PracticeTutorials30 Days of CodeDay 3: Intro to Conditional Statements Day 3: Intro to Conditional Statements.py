"""
Objective
In this challenge, we learn about conditional statements. Check out the Tutorial tab for learning materials and an instructional video.

Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Complete the stub code provided in your editor to print whether or not  is weird.

Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird; otherwise, print Not Weird.

Sample Input 0

3
Sample Output 0

Weird
Sample Input 1

24
Sample Output 1

Not Weird
Explanation

Sample Case 0: 
 is odd and odd numbers are weird, so we print Weird.

Sample Case 1: 
 and  is even, so it is not weird. Thus, we print Not Weird.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

def solution(a):
    b = ['Weird', 'Not Weird']
    
    if a & 1 == 1 :
        return print(b[0])
    else:
        if a >= 2 and a <= 5 :
            return print(b[1])
        if a >= 6 and a <= 20 :
            return print(b[0])
        if a >= 20 :
            return print(b[1])
        else:
            return print(b[1])
            


    
    return

if __name__ == '__main__':
    N = int(input())
    solution(N)
