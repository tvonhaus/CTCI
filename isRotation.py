
# Online Python - IDE, Editor, Compiler, Interpreter

#in: s1 and s2
#out: boolean (is a rotation)

# concatenate s1 with itself
# check if s2 is a substring of concatenated string 1 
# if substring return True

def isRotation(str1,str2):
    concatenated_str = str1 + str1
    if str2 in concatenated_str:
        return True
    return False
    
    
print(isRotation('naveed','eednav'))

print(isRotation('waterbottle','erbottlewat'))

print(isRotation('naveed','taylor'))