def intchecker (a , b, c):
    if a>0 and b>0 and c<0:
       return True
    elif a>0 and b<0 and c>0:
       return True
    elif a<0 and b>0 and c>0:
        return True
    else:
        return False
    
print(intchecker(3, -2, -3))    
     