
#* https://www.hackerrank.com/challenges/py-check-subset/problem

if __name__ == '__main__':
    operations = int(input())
    while operations > 0:
        trash = input()
        set_a = set(map(int, input().split()))
        trash = input()
        set_b = set(map(int, input().split()))
        print(set_a.issubset(set_b))
        operations -= 1
    
    