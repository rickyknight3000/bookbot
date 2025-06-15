from stats import get_book_text
from stats import get_num_words
from stats import get_num_characters

def main():
    text = get_book_text("/home/ratking/workspace/github/rickyknight3000/bookbot/books/frankenstein.txt")
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"{num_words} words found in the document")
    print("--------- Character Count -------")
    print(num_characters)
    return

main()