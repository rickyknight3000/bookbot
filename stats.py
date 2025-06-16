def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def get_num_words(num_words):
    word_count = num_words.split()
    return len(word_count)

def get_num_characters(num_chars):
    num_chars = num_chars.lower()
    char_counts = {}

    for char in num_chars:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_chars(chars):
    sorted_chars = []
    for char, count in chars.items():
        count_dict = {"char": char, "num":count}
        sorted_chars.append(count_dict)
    sorted_chars.sort(reverse=True, key=lambda d: d["num"])
    return sorted_chars
