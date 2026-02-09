
#* https://www.hackerrank.com/challenges/np-min-and-max/problem

import numpy as np

if __name__ == '__main__':
    x, y = tuple(map(int, input().split()))
    x_list = []
    y_list = None
    for i in range(x):
        y_list = list(map(int, input().split()))
        x_list.append(y_list)
    array = np.array(x_list)
    min = np.min(array, axis=1)
    max = np.max(min)
    print(max)
    
        
        
        
    