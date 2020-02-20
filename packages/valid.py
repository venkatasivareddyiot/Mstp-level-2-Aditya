import re

def phoneNoValidator(no):
    pattern='^[6-9][0-9]{9}$|[0][6-9][0-9]{9}$|[+][9][1][6-9][0-9]{9}$'
    if(re.match(pattern,str(no))):
        return True
    return False


def emailValidator(mail):
    pattren='[a-z0-9][a-z0-9._]{4,20}[@][a-z0-9]{3,20}[.][a-z]{2,4}'
    if re.match(pattren,str(mail)):
        return True
    return False