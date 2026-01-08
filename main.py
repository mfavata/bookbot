from stats import get_word_count, get_char_count, sorted_dict
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    num_words = get_word_count(book_text)
    characters = get_char_count(book_text)
    print(f'''============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------''')
    char_dict=sorted_dict(characters)
    for ch in char_dict:
        print(f'{ch["char"]}: {ch["num"]}')
    print('============= END ===============')

main()
