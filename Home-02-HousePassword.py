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



#%% Other Solutions
    
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
 