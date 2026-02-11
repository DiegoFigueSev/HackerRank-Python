
#* https://www.hackerrank.com/challenges/text-alignment/problem

def construct_header(t:int, letter:str):
    max_width = 2*t - 1
    aux_letter = letter
    response = ''
    for _ in range(t):
        response += letter.center(max_width, ' ') + '\n'
        letter = letter + (aux_letter*2)
    return response

#* center = t*3 and pilar = t and 
def construct_pilar(t:int, letter:str):
    response = ''
    width = t + (t*3)
    height = t + 1
    pilar = (letter * t).center(2*t - 1, ' ')
    body = pilar.ljust(width, ' ') + pilar
    for _ in range(height):
        response += body + '\n'
    return response

#* total = 2*t - 1 -> x = (total - t) / 2 
def construct_center(t:int, letter:str):
    body = (letter * (t*3)) + ((letter*t) * 2)
    center_body = body.center((len(body) + (((2*t - 1 - t) // 2))*2), ' ') 
    response = ''
    for _ in range((t+1)//2):
        response += center_body + '\n'
    return response

#* center = t*3
def construct_footer(t:int, letter:str):
    aux = 1
    width = 2*t - 1
    body = letter * (2*t + 1)
    response = body[aux:-aux].center(width, ' ').rjust((t*3) + width + (((2*t - 1 - t) // 2))*2 + 1) + '\n'
    for _ in range(t):
        aux += 1
        response += (body[aux:-aux].center(width, ' ').rjust((t*3) + width + (((2*t - 1 - t) // 2))*2 + 1) + '\n')
        
    return response
    

def solution(t:int, letter:str):
    return construct_header(t, letter) + construct_pilar(t, letter) + construct_center(t, letter) + construct_pilar(t, letter) + construct_footer(t, letter)
    
    

if __name__ == '__main__':
    solution = solution(5, 'H').rstrip()
    print(solution)
    
#* I know, it’s a lot of code; it could be more efficient.