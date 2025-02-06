def palindrome(chaine):
    SatorSquare = ["sator","arepo","tenet","opera","rotas"]
    if chaine in SatorSquare:
        return True
    return chaine == chaine[::-1]
    

print(palindrome("radar"))