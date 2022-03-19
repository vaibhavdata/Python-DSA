import math
import os
import random
import re
import sys
from collections import Counter

if __name__ == '__main__':
    s =sorted(input().strip())
    s_count = Counter(s).most_common()
    s_counts = sorted(s_count,key =lambda x:[x[1]*-1,x[0]])
    for i in range(0,3):
        print(s_counts[i][0],s_counts[i][1])