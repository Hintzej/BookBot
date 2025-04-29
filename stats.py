from collections import Counter


def get_book_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
def count_words(text):
    return len(text.split())

def character_count(text):
    text = text.lower()
    return dict(Counter(text))

def sort_counts(counts):
    count_list = []
    for key in counts:
        temp_dict = {"char": key, "num": counts[key]}
        count_list.append(temp_dict)

    sorted_list = sorted(count_list, key=lambda x: x["num"], reverse=True)
    return sorted_list

def make_report(path):
    text = get_book_text(path)
    count_list = character_count(text)
    sorted_count_list = sort_counts(count_list)
    report_text = f"============ BOOKBOT ============\n" \
                  f"Analyzing book found at {path}...\n" \
                  f"----------- Word Count ----------\n" \
                  f"Found {count_words(text)} total words\n" \
                  f"--------- Character Count -------\n"
    for character in sorted_count_list:
        report_text += f"{character['char']}: {character['num']}\n"
    report_text += "============= END ==============="
    return report_text
