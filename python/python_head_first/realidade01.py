# feito por mim
'''
def longest_word(text):
    tup = text.split()
    tupMaior = 0
    nmTupMaior = ''
    for nome in tup:
        tuptamAux = len(nome)
        if tuptamAux > tupMaior:
            tupMaior = tuptamAux
            nmTupMaior = nome
    return nmTupMaior



print(longest_word("We want a SHRUBBERY"))
print(longest_word("Shrubberies are great"))
'''
# feito pelo site

def longest_word(text):
    return max(text.split(), key=len)

if __name__ == "__main__":
    print(longest_word("We want a SHRUBBERY"))'''