def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def get_num_words(num_words):
    word_count = num_words.split()
    return len(word_count)

def get_num_characters(num_chars):
    num_chars = num_chars.lower()
    char_count = {}

    for char in num_chars:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
