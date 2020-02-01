#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Filtering uppercase chracters in string and concatenate
find_message = lambda text: ''.join(filter(str.isupper, text))


# In[16]:


number = 15
if number % 3==0 and number % 5==0:
    print("done")


# In[19]:


# Fizz Buzz -- if, elif, else 
def checkio(number: int) -> str:
    # Your code here
    # It's main function. Don't remove this function
    # It's using for auto-testing and must return a result for check.

    # replace this for solution
    if not number % 15:
        return 'Fizz Buzz'
    elif not number % 3:
        return 'Fizz'
    elif not number % 5:
        return 'Buzz'
    else :
        return str(number)


# In[15]:


# Indexing even numbers
#1
def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    if len(array) == 0: return 0
    return sum(array[0::2]) * array[-1]


# In[20]:


#2
checkio=lambda x: sum(x[::2])*x[-1] if x else 0


# In[43]:


# Dictionary; Loop and Maximum

def best_stock(a: dict):
    max_price = 0
    res = ""
    for k in a:
        if a[k] >= max_price:
            max_price = a[k]
            res = k
        else: None
    return res

# Best solutions

def best_stock(data):
    return max(data, key=data.__getitem__)

best_stock2 = lambda d: next(k for k, v in d.items() if v == max(d.values()))


# In[81]:


# String; indexing and change strings

def correct_sentence(text: str) -> str:
    """
        returns a corrected sentence which starts with a capital letter
        and ends with a dot.
    """
    if text[0].islower() == True: 
        text = text[0].upper() + text[1:]
    if text[-1] != ".": 
        text = text + "." 
    return text

# Best solutions
def correct_sentence(text: str) -> str:   
    return text[0].upper() + text[1:] + ("." if text[-1] != "." else "")



# In[18]:


# JOIN and REPLACE substrings

def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """
    res=",".join(phrases)
    res = res.replace("right","left")
    return res 

left_join(("left", "right", "left", "stop"))

# Other solutions

def left_join(phrases):
   
    return (','.join(phrases).replace("right", "left"))

left_join(("left", "right", "left", "stop"))


# In[39]:


# Count and Find in strings

def second_index(text: str, symbol: str) -> [int, None]:
    """
        returns the second index of a symbol in a given text
    """
    if text.count(symbol) < 2:
        return None
    else:
        a = text.find(symbol)
        b = text.find(str(symbol), a+1)
    return b

###
import re
def second_index(text: str, symbol: str) -> [int, None]:
    """
        returns the second index of a symbol in a given text
    """
    # your code here
    idx = [m.start(0) for m in re.finditer(symbol, text)]
    return idx[1] if len(idx) > 1 else None

second_index("asdfasdf","s")


# In[48]:


for m in re.finditer("s","asdfasdfasdf"):
    print(m.start(0))


# In[10]:


# Absolute value and Sorted using key

def checkio(numbers_array: tuple) -> list:
    return sorted(numbers_array, key = lambda x: abs(x))
    # return sorted(numbers_array, key = abs)


# In[2]:


# Undefined arguments
def checkio(*args):
# an arbitrary number of arguments 
    return max(args) - min(args) if args else 0


# In[4]:


def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    return text.split()[0]

first_word("hello world")


# In[11]:


def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    d = [".",","]
    for k in d:
        text = text.replace(k," ")
    return text.split()[0]

first_word(" test")


# In[ ]:


def checkio(words: str) -> bool:
    count = 0
    for w in words.split():
        if w.isalpha():
            count += 1
        else: 
            count = 0
        if count == 3:
            return True
            break
    return False

####

import re

def checkio(words: str) -> bool:
    return bool(re.search(r'\s+'.join([r'[^\d\s]+']*3), words))


# In[68]:


a = [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]

def bigger_price(limit: int, data: list) -> list:
    """
        TOP most expensive goods
    """
    return sorted(data,key=lambda x: x['price'], reverse=True)[0:limit]


# In[94]:


def popular_words(text: str, words: list) -> dict:
    # your code here
    res = {}
    for w in words:
        num = text.lower().split().count(w.lower())
        res.update({w : num})
    return res

popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near'])

####

#%%
def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    m1 = text.find(begin)
    m2 = text.find(end)
    return text[m1+1:m2]


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Wow, you are doing pretty good. Time to check it!')
    
#%%
def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    m1 = text.find(begin) + len(begin) if not text.find(begin)==-1 else 0
    m2 = text.find(end) if not text.find(end)==-1 else len(text)
    if m1 > m2:
        return ''
    else:
        return text[m1:m2]

if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
    
#%%
def is_stressful(subj):
    return (subj.isupper() or
            subj.endswith('!!!') or
            any(re.search('+[.!-]*'.join(c for c in word), subj.lower())
                for word in ['help', 'asap', 'urgent']))

if __name__ == '__main__':
    #These "asserts" are only for self-checking and not necessarily for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    print('Done! Go Check it!')
#%%
    
test = 'h--e..l!!,,p urgent'
any(re.search('+[.!-]*'.join(c for c in word), test.lower()) for word in ['help', 'asap', 'urgent'])                

    
    
    
   
    
    
#%%
    
    
from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    # your code here
    return elements==[elements[0]]*len(elements) if elements!=[] else True


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")



#%%

# set() -- Build an unordered collection of unique elements
def all_the_same(elements: List[Any]) -> bool:
    # your code here
    return len(set(elements)) < 2

# all() -- Return True if all elements of the iterable are true (or if the iterable is empty)
    ## any() -- Return True if any element of the iterable is true. If the iterable is empty, return False.
def all_the_same(elements: List[Any]) -> bool:
    # your code here
    return all([elements[i] == elements[i-1] for i in range(1, len(elements))])


#%%
    

# House Password
    
def checkio(data: str) -> bool:
    cond1 = len(data) >= 10
    cond2 = data.isdigit()==False
    cond3 = data.isalpha()==False
    cond4 = data.islower()==False and data.isupper()==False
    return all([cond1,cond2,cond3,cond4])

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")



## Other Solutions
    
import re
def checkio(data: str) -> bool:
    
    digit = len(re.findall(r'\d+', data))       
    upper = len(re.findall(r'[A-Z]+', data))
    lower = len(re.findall(r'[a-z]+', data))
    allData = len(data)
    if(digit>=1 and upper>=1 and lower>=1 and allData>=10):
        return True
    return False

    # r >>> If prefixed, "raw" string notation 
    # \d >>> Matches any Unicode decimal digit
    # + >>> Causes the resulting RE to match 1 or more repetitions of the preceding RE. ab+ will match ‘a’ followed by any non-zero number of ‘b’s; it will not match just ‘a’.
    # 

#%%
    

# The Most Wanted Letter
import string
    
def checkio(text: str) -> str:
    
    split = [char for char in text.lower()]
    
    letters = list(string.ascii_lowercase)
    freq = []
    for i in letters:
        freq.append(split.count(i))
    for k in range(len(freq)):
        if freq[k] == max(freq):
            res = k
            break
    return letters[res]

if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")

#%%
    
def checkio(text):
    text=[char for char in text.lower() if char.isalpha()] #We keep only letters
    chars = {}
    for i in text:
        chars[i] = chars[i]+1 if i in chars.keys() else 1        #Creates a dict with letter as key and count as value

    max_count = max(chars.values())                              
    letters = []                                                 #Creates list of ex-aequo letters
    for letter in chars.items():                                 
        if letter[1] == max_count:                                
            letters.append(letter[0])                            
    return sorted(letters)[0]                                    # We sort them and return the first by alphabetical order


#%%

# Time Converter
    
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

#%%
    
# Other solutions
    
def time_converter(time):
    h, m = [int(i) for i in time.split(':')]
    suffix = h >= 12 and ' p.m.' or ' a.m.'
    h = 12 if h % 12 == 0  else h % 12
    time = str(h)+':'+str(m // 10) + str(m % 10)+suffix
    return time

## // >>> divide and integer output
## % >>> divide and reminder output

#%%    
#%%