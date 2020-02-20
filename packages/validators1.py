import re
def phoneNoValidator(no):
    pattern='^[6-9][0-9]{9}$|[0][6-9][0-9]{9}$|[+][9][1][6-9][0-9]{9}$'
    if(re.match(pattern,str(no))):
        return True
    return False