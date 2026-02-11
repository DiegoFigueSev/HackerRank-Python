import textwrap

DESIGN = '.|.'
SEPARATOR = '-'
MESSAGE = 'WELCOME'

def header(h:int, w:int):
    response = ''
    h = h // 2
    for v in range(h):
        response += (DESIGN*(((v)*2)+1)).center(w, SEPARATOR) + '\n'
    return response
        
def center(w:int):
    return MESSAGE.center(w, SEPARATOR) + '\n'

def footer(h:int, w:int):
    h = (h // 2) - 1
    response = (DESIGN*(((h)*2)+1)).center(w, SEPARATOR) + '\n'
    h -= 1
    while h >= 0:
        response += (DESIGN*(((h)*2)+1)).center(w, SEPARATOR) + '\n'
        h -= 1
    return response
    
def solution(h, w):
    return (header(h, w) + center(w) + footer(h, w)).strip()

if __name__ == '__main__':
    h, w = tuple(map(int, input().split()))
    print(solution(h, w))