def gematria(word: str) -> int:
    gcode = {   'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':600,
                'k':10, 'l':20, 'm':30, 'n':40, 'o':50, 'p':60, 'q':70, 'r':80, 's':90,
                't':100,'u':200,'v':700,'w':900,'x':300,'y':400, 'z':500  }
    try:
        return sum([gcode[char] for char in word])
    except:
        print(word)
        raise ValueError


def gematrix(phrase: str) -> int:
    phrase = strip_accents(phrase.lower())
    phrase = ''.join([i for i in phrase if i.isalpha()])
    try: 
        return sum([gematria(word.lower()) for word in phrase.split(' ')])
    except:
        print(phrase)
        raise ValueError


def strip_accents(s):
    """
    Sanitarize the given unicode string and remove all special/localized
    characters from it.
 
    Category "Mn" stands for Nonspacing_Mark

    (thx http://www.ultrabug.fr/convert-special-characters-to-ascii-in-python/)
    """
    try:
        return ''.join(
            c for c in unicodedata.normalize('NFD', s)
            if unicodedata.category(c) != 'Mn'
        )
    except:
        return s
