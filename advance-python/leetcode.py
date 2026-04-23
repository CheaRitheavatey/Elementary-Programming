def exclusiveTime( n: int, logs: list[str]) -> list[int]:
    result = [0] * n
    stack = []
    prev_time = 0
    for i in range (len(logs)):
        func, string, start = logs[i].split(":")
        if string == "start":
            if stack:
                result[stack[-1]] += start - prev_time
            stack.append(int(func))
            prev_time = start
            
        elif string == "end":
            stack.pop()
            result[stack-1] += start - prev_time + 1
            prev_time = start + 1
            print(result)
    # start -> push into stack
            # -> prev = end - prev
    # end -> pop 
            # -> pop - prev + 1
            # -> append
        
    return result
    
print(exclusiveTime(2, ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]))