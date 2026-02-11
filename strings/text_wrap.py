import textwrap

def wrap(string, max_width):
    response = ''
    i = 0
    f = max_width
    for _ in range(len(string) // max_width):
        response += string[i:f] + '\n'
        i, f = f, f + max_width
    response += string[i:]
    return response

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)