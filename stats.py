def wordCount(text):
    list = text.split()
    num = len(list)
    return num
 
def sort_dict(symb):
    alpha_dict = {}
    for key in symb:
        if key.isalpha():
            alpha_dict[key] = symb[key]  
    symb = alpha_dict
    dict(sorted(symb.items()))
    return symb
    