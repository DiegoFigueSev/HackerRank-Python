
#* https://www.hackerrank.com/challenges/np-mean-var-and-std/problem

import numpy as np

if __name__ == '__main__':
    x, y = tuple(map(int, input().split()))
    x_list = []
    y_list = None
    for i in range(x):
        y_list = list(map(int, input().split()))
        x_list.append(y_list)
    array = np.array(x_list)
    
    #* Numpy mean = Media aritmetica
    mean = np.mean(array, axis=1)
    print(mean)
    
    #* Numpy var = Varianza (que tan alejados estan nuestros puntso de la media)
    var = np.var(array, axis=0)
    print(var)
    
    #* Numpy std = Desviacion standar
    std = round(np.std(array), 11)
    print(std)
        
        
