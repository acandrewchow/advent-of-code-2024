def read_file():
    with open('data.txt', 'r') as f:
        reports = []
        lines = f.read().splitlines()  

        for line in lines:
            levels = list(map(int, line.split()))
            reports.append(levels)

    return reports

def is_safe(levels):
    increasing = None 
    
    for j in range(len(levels) - 1):
        diff = abs(levels[j] - levels[j + 1]) 
        
        if diff < 1 or diff > 3:  
            return False
        
        # Determine if increasing/decreasing
        if increasing is None:
            if levels[j + 1] > levels[j]:
                increasing = True
            elif levels[j + 1] < levels[j]:
                increasing = False
        elif increasing and levels[j + 1] < levels[j]:
            return False
        elif not increasing and levels[j + 1] > levels[j]:
            return False
    
    return True

def solution(reports):
    safe_reports = 0

    for level in reports:
        if is_safe(level):
            safe_reports += 1

    return safe_reports

reports = read_file()
safe_reports = solution(reports)
print(f"Safe Reports: {safe_reports}") 

