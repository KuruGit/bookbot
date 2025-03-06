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
    print(f"found {wordCount(text)} total words")
    print("--------- Character Count -------")
    sorted_dict=sort_dict(count)
    for key, value in sorted_dict.items():
        print(key,": ", value)
    print("============= END ===============")


if __name__ == "__main__":
    main()