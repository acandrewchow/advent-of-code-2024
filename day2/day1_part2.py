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

def check_unsafe_reports(reports):
    safe_reports = 0  

    for levels in reports:
        if is_safe(levels):
            safe_reports += 1  
        # check if report is safe after removal
        else:
            for i in range(len(levels)):
                new_levels = levels[:i] + levels[i+1:]  
                if is_safe(new_levels):
                    safe_reports += 1  
                    break 
    
    return safe_reports

reports = read_file()  
safe_reports = check_unsafe_reports(reports) 
print(f"Safe Reports: {safe_reports}") 