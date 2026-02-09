'''
Lo que realiza la simetrica diferencia es, en dos conjuntos de datos, nos regresa todos los valores que estan tanto
en A como en B pero que no pertenecen a ambas

Basicamente: 
e pertenece a A o B pero no a ambas  
'''

if __name__ == '__main__':
    a = int(input())
    b = set(map(int, input().split()))
    a = int(input())
    c = set(map(int, input().split()))
    print(len(b.symmetric_difference(c)))