def string_alternative(instr):
    # count = 0
    retStr = ""
    for i in range(len(instr)):
        if i % 2 == 0 :
            retStr += instr[i]

    return retStr

userString = input("Please input a string: ")

print(string_alternative(userString))