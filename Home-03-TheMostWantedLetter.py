import string

def checkio(text: str) -> str:
    split = [char for char in text.lower()]
    letters = list(string.ascii_lowercase)
    freq=[]
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

#%% Other solutions
    
def checkio(text):
    text=[char for char in text.lower() if char.isalpha()]       # We keep only letters
    chars = {}
    for i in text:
        chars[i] = chars[i]+1 if i in chars.keys() else 1        # Creates a dict with letter as key and count as value

    max_count = max(chars.values())                              
    letters = []                                                 # Creates list of ex-aequo letters
    for letter in chars.items():                                 
        if letter[1] == max_count:                                
            letters.append(letter[0])                            
    return sorted(letters)[0]                                    # We sort them and return the first by alphabetical order
