def wordCount(text):
    list = text.split()
    num = len(list)
    return num
 
def sort_dict(dict):
    for key in dict:
        if !key.isalpha():
            del dict[key]
    dict(sorted(dict.items()))
    return dict
    