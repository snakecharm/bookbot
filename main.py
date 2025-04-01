import sys
from stats import word_count
from stats import character_count
from stats import sorted_list

def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
    return contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    num_words = word_count(text)
    print(f"Found {num_words} total words")
    letter_count = sorted_list(character_count(text))
    print("--------- Character Count -------")
    for item in letter_count:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")
main()