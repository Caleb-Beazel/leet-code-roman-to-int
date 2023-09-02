def romanToInt(s):

    converted_vals = []
    converted_to_int = 0

    for letter in s:
        if letter == 'I':
            converted_vals.append(1)
        elif letter == 'V':
            converted_vals.append(5)
        elif letter == 'X':
            converted_vals.append(10)
        elif letter == 'L':
            converted_vals.append(50)
        elif letter == 'C':
            converted_vals.append(100)
        elif letter == 'D':
            converted_vals.append(500)
        elif letter == 'M':
            converted_vals.append(1000)
    
    for i in range(len(converted_vals) - 1):
        if converted_vals[i] >= converted_vals[(i+1)]:
            converted_to_int += converted_vals[i]
        elif converted_vals[i] < converted_vals[(i+1)]:
            converted_to_int -= converted_vals[i]

    converted_to_int += converted_vals[-1]

            

    return converted_to_int


print(romanToInt("MCMVIII"))
print(romanToInt("LVIII"))
