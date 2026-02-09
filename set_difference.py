
#* https://www.hackerrank.com/challenges/py-set-difference-operation/problem?isFullScreen=true

'''
Lo que realiza la diferencia es, en dos conjuntos de datos, nos regresa todos los valores que estan en A pero no en B

Basicamente: 
e pertenece a A - B
'''

if __name__ == '__main__':
    a = int(input())
    b = set(map(int, input().split()))
    a = int(input())
    c = set(map(int, input().split()))
    print(len(b.difference(c)))