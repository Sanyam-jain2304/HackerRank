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
    dlr,drl=(0,0)
    for k in range(len(arr)):
        dlr+=arr[k][k]
    i=0
    j=len(arr)-1
    while(j>-1):
        print(arr[i][j])
        drl+=arr[i][j]
        i+=1
        j-=1
    return abs(dlr-drl)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
