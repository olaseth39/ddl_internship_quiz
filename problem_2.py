#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    #print(n)
    for i in range(1, n+1):
        #use rjust to make it right alligned
        print( ('#'*i).rjust(n))

if __name__ == '__main__':
    n = int(input())

    staircase(n)
