import sys
from stats import analyze_book_stats

def get_book_text(file_path):
    contents = ""
    print(f"Analyzing book found at {file_path}...")
    with open(file_path) as file:
        contents = file.read()
    return contents

def check_input_args():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        return sys.argv[1]

def main(): 
    print("============ BOOKBOT ============")
    book_path = check_input_args()
    text = get_book_text(book_path)
    analyze_book_stats(text)
    print("============= END ===============")

main()