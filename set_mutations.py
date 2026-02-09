
#* https://www.hackerrank.com/challenges/py-set-mutations/problem

def options(op:str, prin_set:set, sec_set:set):
    match op:
        case 'update':
            prin_set.update(sec_set)
        case 'intersection_update':
            prin_set.intersection_update(sec_set)
        case 'difference_update':
            prin_set.difference_update(sec_set)
        case 'symmetric_difference_update':
            prin_set.symmetric_difference_update(sec_set)

if __name__ == '__main__':
    aux = input()
    principal_set = set(map(int, input().split()))
    quantity_operations = int(input())
    while (quantity_operations > 0):
        request = input().split()
        op = request[0]
        secondary_set = set(map(int, input().split()))
        options(op, principal_set, secondary_set)
        quantity_operations -= 1
    print(sum(principal_set))
        
    
