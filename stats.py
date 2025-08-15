import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents 

def word_count():
    contents = get_book_text(sys.argv[1])
    list_words = contents.split()
    num_words = len(list_words)
    return num_words 

def count_characters():
    # converted to lowercase, got list of characters, made empty dictionary to count duplicates
    contents = get_book_text(sys.argv[1])
    lowercase_contents = contents.lower()
    lowercase_chars = list(lowercase_contents)
    chars_dict = {}
    for char in lowercase_chars:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict

def sort_on(items):
    return items["num"]

def nested_dictionary(dictionary):
    nested_dict = []
    for char, count in dictionary.items():
        nested_dict.append({"char": char, "num": count})
    nested_dict.sort(reverse = True, key = sort_on)
    return nested_dict
    
    
    