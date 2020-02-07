def unique(data) -> list: 
    res = [] 
    for x in data:
        if x not in res:
            res.append(x)
    return res
    
def repeat(x,n) -> list:
    res=[]
    for i in range(n):
        res.append(x)
    return res

def frequency_sort(items) -> list:
    elements = unique(items)
    freq = [items.count(e) for e in elements]
    freq_ordered = sorted(unique(freq), reverse=True)
    res = []
    for ref in freq_ordered:
        for ind in range(len(freq)):
            if freq[ind]==ref:
                res += repeat(elements[ind], ref)
    return res

if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")

#%% Other solutions

def frequency_sort(items):
    # your code here
    ret=[]
    set1=set(items)
    list_wcnt=[(x,items.count(x),items.index(x)) for x in set1]
    sorted_list=sorted(list_wcnt,key=lambda x:(1/x[1],x[2]),reverse=False)
    
    for e in sorted_list:
        ret += [e[0] for x in range(e[1])]
    return ret

# list_name.index(element, start, end)
# sorted(... , key = "any functions for customized ordering")



from collections import Counter

def frequency_sort(items):
    # your code here
    my_list = Counter(items).most_common()
    list_temp = []
    for x, y in my_list:
        for _ in range(y):
            list_temp.append(x)
    return list_temp


