
#* https://www.hackerrank.com/challenges/py-check-strict-superset/problem

def solution():
    principal_set = set(map(int, input().split()))
    q_op = int(input())
    while q_op > 0:
        q_op -= 1
        sec_set = set(map(int, input().split()))
        if not principal_set.issuperset(sec_set):
            return False
    return True

if __name__ == '__main__':
    print(solution())
    
    
    
    