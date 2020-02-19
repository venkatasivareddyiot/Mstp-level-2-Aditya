def phoneValidator(no):
    sn=str(no)
    l=len(sn)
    if (l==10 and(sn[0]=='9' or sn[0]=='8'or sn[0]=='7' or sn[0]=='6')):
        return True
    if(l==11 and sn[0]=='0' and (sn[1]=='9' or sn[1]=='8'or sn[1]=='7' or sn[1]=='6')):
        return True
    if(l==13 and sn[0]=='+' and sn[1:3] =='91' and (sn[3]=='9' or sn[3]=='8'or sn[3]=='7' or sn[3]=='6')):
       return True
    else:
       return False