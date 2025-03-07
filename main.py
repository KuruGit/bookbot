import sys
from stats import wordCount
from stats import sort_dict
from collections import Counter

def getBook(path_to_file):
    with open(path_to_file) as file:
        text = file.read()
    return text

def filepath(args):
    path = ""
    if len(args) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = args[1]
    return path

def main():
    bookPath = filepath(sys.argv)  
    text = getBook(bookPath)
    text2 = text.lower()
    count = Counter(text2)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookPath}...")
    print("----------- Word Count ----------")
    print(f"Found {wordCount(text)} total words")
    print("--------- Character Count -------")
    sorted_dict=sort_dict(count)
    for key, value in sorted_dict.items():
        print(f"{key}: {value}")
    print("============= END ===============")


if __name__ == "__main__":
    main()