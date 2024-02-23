def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
        print_a_report(file_contents, book_path)
        

def get_word_count(text):
    return len(text.split())

def get_letter_count(text):
    lowered_text = text.lower()
    text_dic = {}
    for letter in lowered_text:
        if letter.isalpha():
            if letter in text_dic:
                text_dic[letter] += 1
            else:
                text_dic[letter] = 1
    sorted_dic = sorted(text_dic.items(), key=lambda item: item[1], reverse=True)
    return sorted_dic


def print_a_report(text, path):
    print(f"--- Begin report of {path} ---")
    print(f"{get_word_count(text)} words found in the document")
    print("")
    for letter in get_letter_count(text):
        print (letter)
    print("--- End report ---")

main()