def time_converter(time):
    split = time.split(":")
    h = int(split[0])
    m = int(split[1])
    minutes = h*60+m
    if minutes==0:
        return '12:00 a.m.'
    if minutes<720:
        return str(h)+':'+split[1]+ ' a.m.'
    if 720<= minutes < 780:
        return str(h)+':'+split[1]+ ' p.m.'
    else:
        return str(h-12)+":"+split[1]+' p.m.' 

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")

#%% Other solutions
    
def time_converter(time):
    h, m = [int(i) for i in time.split(':')]
    suffix = h >= 12 and ' p.m.' or ' a.m.'
    h = 12 if h % 12 == 0  else h % 12
    time = str(h)+':'+str(m // 10) + str(m % 10)+suffix
    return time

## // >>> divide and integer output
## % >>> divide and reminder output
