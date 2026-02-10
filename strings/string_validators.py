
#* https://www.hackerrank.com/challenges/string-validators/problem

if __name__ == '__main__':
    s = input()
    has_alnum = False
    has_alpha = False
    has_digit = False
    has_lower = False
    has_upper = False
    for letter in s:
        has_alnum = has_alnum or letter.isalnum()
        has_alpha = has_alpha or letter.isalpha()
        has_digit = has_digit or letter.isdigit()
        has_lower = has_lower or letter.islower()
        has_upper = has_upper or letter.isupper()
    print(has_alnum)
    print(has_alpha)
    print(has_digit)
    print(has_lower)
    print(has_upper)