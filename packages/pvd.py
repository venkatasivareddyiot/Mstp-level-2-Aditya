import re
def pvd1(no):
    patteren='^[6-9][0-9]{9}$|[0][6-9][0-9]{9}$|[+][9][1][6-9][0-9]{9}$'
    if re.match(patteren,str(no)):
        return True
    return False