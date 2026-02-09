
#* https://www.hackerrank.com/challenges/py-the-captains-room/problem

if __name__ == '__main__':
    group_size = int(input())
    people = list(map(int, input().split()))
    aux_dicc = dict()
    response = None
    aux_response = dict()
    for val in people:
        if val in aux_dicc:
            aux_dicc[val] = aux_dicc[val] + 1
            if (val in aux_response):
                del aux_response[val]
        else: 
            aux_dicc[val] = 1
            aux_response[val] = True
    print(list(aux_response.keys())[0])
    