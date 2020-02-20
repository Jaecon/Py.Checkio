def long_repeat(line: str) -> int:
    if len(line)==0:
        return 0
    else:
        res = []
        rep_char = line[0]
        cnt = 0
        for char in line:
            if char == rep_char:
                cnt += 1
            else:
                res.append(cnt)
                cnt = 1
                rep_char = char
    return max(res) if res!=[]  else cnt

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')

#%% Other Solutions

def long_repeat(line: str) -> int:
    """
        length the longest substring that consists of the same char
    """
    num = 0
    maxnum = 1
    keychr = ""
    
    if not line: return 0
    else:
        for chara in line:
            if keychr != chara:
                keychr = chara
                num = 1
            else:
                num += 1
                maxnum = max(num, maxnum)
    return maxnum



import re


def long_repeat(line: str) -> int:    
    # Maximum repeat of each letter (Example: it will convert 'sdsffffse' to ['s', 'd', 'e', 'ffff'])
    split_line = [max(re.findall(fr'{letter}+', line)) for letter in set(list(line))]
    
    # Return length of longest string in 'split_line' or 0 if it empty 
    return len(max(split_line, key = len)) if split_line else 0

# 'f' prefix >>> Formatted string literals
