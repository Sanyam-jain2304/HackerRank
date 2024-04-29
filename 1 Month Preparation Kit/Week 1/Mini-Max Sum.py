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
    arr.sort()
    min = 0
    max = 0
    for i in range(len(arr)-1):
        min += arr[i]
    for i in range(len(arr)-1, 0, -1):
        max += arr[i]
        
    print(str(min) + " " + str(max))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
