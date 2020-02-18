import re

def flat_list(array):
    listed_str_array = re.split("[[\],\s]+", str(array))[1:-1]
    res = []
    for char in listed_str_array:
      res.append( int(char) )
    return res

if __name__ == '__main__':
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')


#%% Other Solutions

def flat_list(array):
    new_list = []
    for elem in array:
        if isinstance(elem,list):
            new_list.extend(flat_list(elem))
        else:
            new_list.append(elem)
    return new_list

# Signature: isinstance(obj, class_or_tuple)
# Docstring:
# Return whether an object is an instance of a class or of a subclass thereof.
#
# list.append() '''adds itis argument as a single element to the end of the list'''
# list.extend() '''iterates over its argument adding each element to the list'''