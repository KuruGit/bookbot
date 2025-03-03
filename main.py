def getBook(path_to_file):
    with open(path_to_file) as file:
        text = file.read()
    return text
def main():
    text = getBook('books/frankenstein.txt')
    print(text)

if __name__ == "__main__":
    main()