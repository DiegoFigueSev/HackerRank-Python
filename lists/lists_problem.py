
#? https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

#* Codigo base

def myAppend(n:int, l):
    l.append(n)

def myInsert(n, i, l):
    l.insert(i, n)

def myRemove(n, l):
    l.remove(n)
    
def myPrint(l):
    print(l)

'''
insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
'''

def option(e: str, response : list = []):
    data = e.split()
    
    req, val, i = (data + [None, None, None])[:3]
    val = val and int(val)
    i = i and int(i)

    match req:
        case 'insert':
            myInsert(i, val, response)
        case 'print':
            print(response)
        case 'remove':
            myRemove(val, response)
        case 'append':
            myAppend(val, response)
        case 'sort':
            response.sort()
        case 'pop':
            response.pop()
        case 'reverse':
            response.reverse()
    

if __name__ == '__main__':
    N = int(input())
    response = []
    for i in range(N):
        M = str(input())
        option(M, response)
        
    
