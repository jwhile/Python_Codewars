def to_jaden_case(string):
    stringsplit=string.split()
    stringjoin=" "
    for i in range(0,len(stringsplit)):
        stringsplit[i] = stringsplit[i].capitalize()
    return (stringjoin.join(stringsplit))


"""

def toJadenCase(string):        
    return " ".join(w.capitalize() for w in string.split())
"""
"""
import string

def to_jaden_case(string):
    return string.capwords()
"""
print(to_jaden_case("How can mirrors be real if our eyes aren't real"))

