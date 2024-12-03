import re

def read_file():
    with open('data.txt', 'r') as f:
        data = f.read()
    return data

def solution(data):
    matches = re.findall(r"mul\((\d+),\s*(\d+)\)", data)
    result = 0 
    for num1, num2 in matches:        
        result += int(num1) * int(num2)

    return result

data = read_file()
result = solution(data)
print(result)