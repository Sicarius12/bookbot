def get_book_text(filepath):
    contents = ""
    with open(filepath) as f:
        contents = f.read()

    return contents

def get_num_words(filepath):
    words = get_book_text(filepath).split()

    return len(words)

def get_num_characters(filepath):
    character_dict = {}
    text = get_book_text(filepath).lower()
    for character in text:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1

    return character_dict