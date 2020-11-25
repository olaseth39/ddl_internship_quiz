#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    # my codes start here
    n = len(ar)
    print(n)
    for i in ar:
        print(i)
    sum = 0
    for j in range(n):
        sum += ar[j]
    return sum
    # my codes ends here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
