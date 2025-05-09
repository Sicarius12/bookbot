def get_book_text(filepath):
    contents = ""
    with open(filepath) as f:
        contents = f.read()

    return contents

def get_num_words(filepath):
    words = get_book_text(filepath).split()

    return len(words)