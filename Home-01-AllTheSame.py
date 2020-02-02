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


#%% Other solutions
 
# set() -- Build an unordered collection of unique elements
def all_the_same(elements: List[Any]) -> bool:
    # your code here
    return len(set(elements)) < 2

# all() -- Return True if all elements of the iterable are true (or if the iterable is empty)
# any() -- Return True if any element of the iterable is true. If the iterable is empty, return False.
def all_the_same(elements: List[Any]) -> bool:
    # your code here
    return all([elements[i] == elements[i-1] for i in range(1, len(elements))])
