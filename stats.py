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

# def sort_on(dict):
#     return dict["num"]

def get_sorted_dictionary(filepath):
    character_dict = get_num_characters(filepath)
    dictionary_list = []

    # for character in character_dict:
    #     count = character_dict[character]
    #     dictionary_list.append({"char": character, "num": count})

    for key, value in character_dict.items():
        if key.isalpha():
            dictionary_list.append({"char": key, "num": value})

    dictionary_list.sort(reverse=True, key=lambda x: x["num"])

    return dictionary_list

# def get_sorted_dictionary(filepath):
#     character_dict = get_num_characters(filepath)

#     # This returns a list of tuples (character, count) sorted by count
#     sorted_items = sorted(character_dict.items(), key=lambda x: x[1], reverse=True)

#     # Filter to only include alphabetical characters
#     alpha_items = [item for item in sorted_items if item[0].isalpha()]

#     return alpha_items