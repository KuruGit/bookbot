def getBook(path_to_file):
    with open(path_to_file) as file:
        text = file.read()
    return text

def wordCount(text):
    list = text.split()
    num = len(list)
    return num 

def main():
    text = getBook('books/frankenstein.txt')
    print(text)
    print(f"{wordCount(text)} words found in the document")

if __name__ == "__main__":
    main()