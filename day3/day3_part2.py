import re

def read_file():
    with open('data.txt', 'r') as f:
        data = f.read()
    return data

def solution(data):
    mul_pattern = r"mul\((\d+),\s*(\d+)\)"  
    do_pattern = r"do\(\)"  
    dont_pattern = r"don\'t\(\)"  

    mul_enabled = True 
    result = 0
    i = 0  

    while i < len(data):
        # checks for mul(num1, num2) pattern
        if re.match(mul_pattern, data[i:]) and mul_enabled:
            match = re.match(mul_pattern, data[i:])
            num1, num2 = match.groups()
            result += int(num1) * int(num2)
            i += match.end()  # moves past the matched 'mul()'
        
        # Check for 'do()' instruction
        elif re.match(do_pattern, data[i:]):
            mul_enabled = True
            i += len("do()")  # Skip 'do()'
        
        # Check for 'don't()' instruction
        elif re.match(dont_pattern, data[i:]):
            mul_enabled = False
            i += len("don't()")  # Skip 'don't()'
        else:
            i += 1

    return result

data = read_file()
result = solution(data)
print(result)  