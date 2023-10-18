def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    text_str = text_to_string(text)
    text_str_lower = text_str.lower()
    character_count = count_letters(text_str_lower)
    print(character_count)


def count_letters(text):
    # Crear un diccionario vacío
    dict = {}
    for letter in text:
        if letter in dict:
            dict[letter] = dict[letter] + 1
        else:
            dict[letter] = 1
    return dict


def text_to_string(text):
    text_str = str(text)
    return text_str


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
