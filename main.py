from stats import wordCount
from stats import sort_dict
from collections import Counter

def getBook(path_to_file):
    with open(path_to_file) as file:
        text = file.read()
    return text

def main():
    text = getBook('books/frankenstein.txt')
    text2 = text.lower()
    count = Counter(text2)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"{wordCount(text)} words found in the document")
    print("--------- Character Count -------")
    print(sort_dict(count))
    print("============= END ===============")


if __name__ == "__main__":
    main()