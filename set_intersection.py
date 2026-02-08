
#* https://www.hackerrank.com/challenges/py-set-intersection-operation/problem?isFullScreen=true

import sys

if __name__ == '__main__':
    a = int(input())
    b = set(map(int, input().split()))
    a = int(input())
    c = set(map(int, input().split()))
    print(len(b.intersection(c)))

    
