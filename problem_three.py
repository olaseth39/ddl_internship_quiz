#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
   
    print(b, len(keyboards), len(drives))
    for keyboard in keyboards:
        print(keyboard)
    for drive in drives:
        print(drive)
        
    all_sum = []
    for num1 in keyboards:
        for num2 in drives:
            sum = num1 + num2
            all_sum.append(sum)
    
    all_sum_less_than_b = []
    for i in all_sum:
        if i <= b:
            all_sum_less_than_b.append(i)

    if all_sum_less_than_b == []:
        return -1
    else:
        return max(all_sum_less_than_b)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
