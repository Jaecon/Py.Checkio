import string

def safe_pawns(pawns: set) -> int:
    cnt = 0
    abc = string.ascii_lowercase
    for place in pawns:
        index = abc.index(place[0])
    
        col = [abc[index-1], abc[index+1]]  
        row = str(int(place[1]) - 1)
        defence = {col[0]+row, col[1]+row}
    
        if not pawns.isdisjoint(defence):
            cnt += 1
    return cnt

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")