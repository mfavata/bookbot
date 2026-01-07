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
