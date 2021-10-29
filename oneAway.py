def replacement(str1,str2):
    count = 0
    if((len(str1) - len(str2)) > 1):
        return False
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1
    #if one char is different, return True
    if count == 1:
        return True
    return False
    
def insertion(str1,str2):
    index1 = 0
    index2 = 0
    while (index1 < len(str1) and index2 < len(str2)):
        print(index1,index2)
        print(str1[index1],str2[index2])
        if(str1[index1] != str2[index2]):
            if(index1 != index2):
                return False
            index2 += 1
        else:
            index1 += 1 
            index2 += 1
    return True
    
    
def oneEditAway(str1,str2):
    if(len(str1) == len(str2)):
        return replacement(str1,str2)
    if((len(str1) - len(str2)) == -1):
        return insertion(str1,str2)
    if((len(str1) - len(str2)) == 1):
        return insertion(str2,str1)
    else:
        return False

print(oneEditAway('aimilll','aimillll'))