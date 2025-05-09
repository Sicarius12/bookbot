from stats import get_num_words

def main():
    num_words = get_num_words("./books/frankenstein.txt")
    print(f"{num_words} words found in the document")

main()