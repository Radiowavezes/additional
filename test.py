strs = ["car","cir",'car']

def roman(strs):
    strs = sorted(set(strs), key=len)
    res_str = ''
    let = -1
    if len(strs) == 1:
            return strs[0]
    else:
        for letter in strs[0]:
            matches = 1
            let += 1
            for word in strs[1:]:
                if letter == word[let]:
                    matches += 1
                    if matches == len(strs):
                        res_str += letter
                else:
                    break
            else:
                continue
            break
    return res_str

print(roman(strs))
