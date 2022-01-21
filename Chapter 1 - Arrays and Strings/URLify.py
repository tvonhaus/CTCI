
# Online Python - IDE, Editor, Compiler, Interpreter

def URLify(string):
    newString = ""
    for c in string:
        if (c == " "):
            newString = newString + "%20"
        else:
            newString = newString + c 
    print(newString)
    return (newString)


URLify('taylor von hausen     ')