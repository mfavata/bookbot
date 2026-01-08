def sort_on(items):
    return items["num"]

def get_word_count(file_contents):
    words = file_contents.split()
    return len(words)

def get_char_count(file_contents):
    char_dict = {}
    file_contents = file_contents.lower()
    
    for i in range(len(file_contents)):
        if file_contents[i] in char_dict:
            char_dict[file_contents[i]] += 1
        else:
            char_dict[file_contents[i]] = 1

    return char_dict

def sorted_dict(characters):
    sorted_chars = []
    for char in characters:
        if char.isalpha():
            char_dict = {"char": char, "num": characters[char],}
            sorted_chars.append(char_dict)
    
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars
