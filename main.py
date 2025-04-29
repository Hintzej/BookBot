from stats import count_words, character_count, sort_counts, make_report
import sys

def get_book_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def main():
    # book_text = get_book_text("books/frankenstein.txt")
    # num_words = count_words(book_text)
    # print(f"{num_words} words found in the document")
    # print(character_count(book_text))
    # print(sort_counts(character_count(book_text)))
    if len(sys.argv) is not 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    report = make_report(sys.argv[1])
    print(report)

if __name__ == '__main__':
    main()