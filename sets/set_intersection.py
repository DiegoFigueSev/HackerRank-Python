
#* https://www.hackerrank.com/challenges/py-set-intersection-operation/problem?isFullScreen=true

import sys

#? Interseccion 

'''
Lo que realiza la interserccion es, en dos conjuntos de datos, nos regresa todos los valores que estan tanto
en A como en B

Basicamente: 
e pertenece a A y B
'''

if __name__ == '__main__':
    a = int(input())
    b = set(map(int, input().split()))
    a = int(input())
    c = set(map(int, input().split()))
    print(len(b.intersection(c)))

    
