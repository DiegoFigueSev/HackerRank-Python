
#* https://www.hackerrank.com/challenges/np-min-and-max/problem

import numpy as np

if __name__ == '__main__':
    x = int(input())
    a_matrix = []
    b_matrix = []
    index = 1
    while index <= 2:
        for i in range(x):
            if index == 1:
                y = list(map(int, input().split()))
                a_matrix.append(y)
            else:
                y = list(map(int, input().split()))
                b_matrix.append(y)
        index += 1
    
    a_matrix = np.array(a_matrix)
    b_matrix = np.array(b_matrix)
    
    print(np.dot(a=a_matrix, b=b_matrix))
    
    
    
        
        
        
    