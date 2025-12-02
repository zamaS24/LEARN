class Pillow(object): 

    def __init__(self, name='defeault'): 
        self.name = name


    def __str__(self) -> str:
        return self.name 
    
    def __call__(self, *args, **kwds):
            for arg in args: 
                print(arg)
            print()
            for key, value in kwds.items(): 
                print(f'key: {key}, val: {value}')



"""
re.finditer(pattern, text) -> matches (obj) 
    match.group : the string
    match.start() : start index of the match in the text
    match.end() : end index of the match in the text

    
re.split('pattern', text): return list of splitted words based on pattern
    example splitting by space re.split('\s', text)
    
? : zero or one 
+ : one or more 
* : zero or more 
{n} : exactly n
a|b : a or b 


^ : start of string 
$ : end of string 

\b : not part of a larger word

"""


import re 

# TODO: 
# learn about regex
# find a pattern in a txt with it's position in text




txt = """8924 
202304159968-TT1256 There is something today if you want to make it in the 1234 / for the &ed; for the rest of the world can you feel me brother on how this can be worked S-SI and the S-LS and also S-VOIP !!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!! 

********************
********************
********************
********************
"""

# rex = r"\b\d+\b"    # r to tell it to be raw string, so that it can use the \b  and all 
# rex = r'\b[A-Z]{1}-[A-Z]{4}\b'

matches = re.finditer(rex, txt)
for match in matches: 
    str_match = match.group()
    start = match.start()
    end = match.end()

    print(f' match : {str_match}, start : {start}, end : {end}')



# splitted = re.split(rex, txt)
# print(' splitted is \n', splitted)



"""Algortihme


- define begin and end indexes of the ticket
- retrive the ticket 
"""




def has2spaces(str:str): 
    return bool(re.search(r' {2}', str))


def test_has2spaces(str:str) -> None: 

    test_string1 = 'this string has  two spaces lol'
    test_string2 = 'this string has only one spaces'
    test_string3 = '' 
    test_string4 = ' '

    print(has2spaces(test_string1))
    print(has2spaces(test_string2))
    print(has2spaces(test_string3))
    print(has2spaces(test_string4))







def extract_ticket(): 
    pass 


