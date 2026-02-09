
#* https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):
    index = 0
    total = 0
    while index < len(string) - len(sub_string) + 1:
        if string[index:index+len(sub_string)] == sub_string:
            total += 1
        index += 1
    return total

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)