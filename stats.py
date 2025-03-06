def wordCount(text):
    list = text.split()
    num = len(list)
    return num
 
def sort_on(dict):
    return dict["key"]

def sort_dict(dict):
    alpha_dict = []
    for key in dict:
        if key.isalpha():
            alpha_dict.append(key) 
    alpha_dict.sort(reverse=True, key=sort_on)
    return alpha_dict
    