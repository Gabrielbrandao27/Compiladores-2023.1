with open("source.txt", "r") as f:
    tabela= []

    for code in f:
        index = 0
        aux = ""
        atom = ""
        variable = ""
        numeral = ""
        i = code[index]


        while index < len(code):

            if i.isalpha():
                    
                if i.islower():
                    atom += i
                    while index+1 < len(code) and (code[index+1]).islower():
                        atom += code[index+1]
                        index += 1
                    if [atom, "atom"] not in tabela:
                        tabela.append([atom, "atom"])
                    i = code[index+1]


                elif i.isupper():
                    variable += i
                    while index+1 < len(code) and ((code[index+1]).isalpha() or (code[index+1]).isnumeric()):
                        variable += code[index+1]
                        index += 1

                    if [variable, "variable"] not in tabela:
                        tabela.append([variable, "variable"])
                    i = code[index+1]


            elif i.isnumeric():
                numeral += i
                while index+1 < len(code) and (code[index+1]).isnumeric():
                    numeral += code[index+1]
                    index += 1

                if code[index+1] == '.':
                    if (code[index+2]).isnumeric():
                        numeral += code[index+1] + code[index+2]
                        while index+1 < len(code) and (code[index+1]).isnumeric():
                            numeral += code[index+1]
                            index += 1

                        if code[index+1] == 'Ǝ':
                            if code[index+2] == '-':
                                numeral += code[index+1] + code[index+2]
                                while index+1 < len(code) and (code[index+1]).isnumeric():
                                    numeral += code[index+1]
                                    index += 1

                if [numeral, "numeral"] not in tabela:
                    tabela.append([numeral, "numeral"])
                i = code[index+1]
                

            elif i == "?":
                aux += i
                if code[index+1] == "-":
                    aux += code[index+1]
                
                if [aux, "?-"] not in tabela:
                    tabela.append([aux, "?-"])
                i = code[index+1]
            
            elif i == ":":
                aux += i
                if code[index+1] == "-":
                    aux += code[index+1]

                if [aux, ":-"] not in tabela:
                    tabela.append([aux, ":-"])
                i = code[index+1]


            elif i == "(":
                if ['(', '('] not in tabela:
                    tabela.append([i, '('])
                i = code[index+1]

            elif i == ")":
                if [i, ')'] not in tabela:
                    tabela.append([i, ')'])
                i = code[index+1]

            elif i == ".":
                if [i, '.'] not in tabela:
                    tabela.append([i, '.'])
                i = code[index+1]

            index += 1

result = ""
for i in range(len(tabela)):
    result += str(tabela[i])
    if i < len(tabela) - 1:
        result += "\n"
print(result)