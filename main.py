from stats import word_count, char_count, dict_sort
import sys

def main():
    if len(sys.argv) > 1:        
        book_path = sys.argv[1]
        count_list = dict_sort(char_count(get_book_text(book_path)))
        
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count(get_book_text(book_path))} total words")
        print("--------- Character Count -------")

        for item in count_list:
            print(f"{item['Character']}: {item['Count']}")    
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


main()