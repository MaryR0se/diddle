# Wordle helper :)

from english import ENGLISH_WORDS

def helper(gren, yllo, ydct, grey):

    def inpsbl(word, gren, yllo, ydct, grey):
        if len(word) != 5:
            return False
        for i in range(5):
            if gren[i].isalpha():
                if not word[i] == gren[i]:
                    return False
        for letr in yllo:
            if not letr in word:
                return False
            for i in range(5):
                if word[i] == letr and str(i + 1) in ydct[letr]:
                    return False
        for letr in grey:
            if letr in word:
                return False
        return True
     
    wrds = ENGLISH_WORDS
    psbl = [] #possible
    for word in wrds:
        if inpsbl(word, gren, yllo, ydct, grey):
            psbl.append(word)
    return psbl

def ylonot(yllo):
    ydct = {}
    for letr in yllo:
        ydct[letr] = input('\nPlease enter the place in the word (from 1 to 5) where you know the letter "' + letr + '" is not placed.\nDo not separate with commas, spaces, etc. - numbers only.\n')
    return ydct

if __name__ == "__main__":
    gren = input("\nPlease enter five characters.\nEnter the letters showing up in green in their respective places.\nFill in the rest with non-letter characters.\n")
    yllo = input("\nPlease enter any letters that show up in yellow.\nDo not separate with commas, spaces, etc. - letters only.\n")
    ydct = ylonot(yllo)
    grey = input("\nPlease enter all the letters you know are not in the word.\nDo not separate with commas, spaces, etc. - letters only.\n")
    print(helper(gren, yllo, ydct, grey))