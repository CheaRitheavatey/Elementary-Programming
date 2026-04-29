# def encode(strs: list[str]) -> str:
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y','z']
inputs = ["hello", "world", "apple"] # "hello\nworld\napple"
inputss = ("\n".join(inputs))
print(inputss)
new_words = ""
for i in inputss:
    if i == "\n":
        new_words = new_words.rstrip()
        new_words+= "\n"
        continue
    num = (ord(str(i)))
    new_words += str(num) + " "
    print(f"{i} = {ord(str(i))}")
    
    # 10 = new words
array = []
print(new_words)
print(chr(111))
word = ""

words = new_words.split("\n")
print(new_words)
print(words)
for i in words:
    print(i)
    c = i.split(" ")
    print(c)
    for char in c:
        if char == "":
            continue
        
        word += (chr(int(char)))
        print(word)
    array.append(word)
    word = ""
print(array)
def topKFrequent(nums: list[int], k: int) -> list[int]:
        # k will be the len of the output arr
        store = {}
        result = []
        x = 0
        for i in nums:
            store[i] = store.get(i,0) + 1
        print(store)
        
        while x <= k-1:
            for i in sorted(store.values())[::-1]:
                result.append(i)
            x+=1
        return result
        
        
        


        
print(topKFrequent([1,4,4,4,7,7],2))
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