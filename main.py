from stats import get_num_words
from stats import get_num_characters
from stats import get_sorted_dictionary

def main():
    import sys

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    num_words = get_num_words(sys.argv[1])
    #num_characters = get_num_characters("./books/frankenstein.txt")
    num_characters_sorted = get_sorted_dictionary(sys.argv[1])
    # print(f"{num_words} words found in the document")
    # print(num_characters_sorted)

    # Print the header
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")

    # Print word count section
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    # Print character count section
    print("--------- Character Count -------")
    for sorted_char in num_characters_sorted:
        print(f"{sorted_char["char"]}: {sorted_char["num"]}")

    # Print the footer
    print("============= END ===============")

main()