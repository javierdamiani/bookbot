def main():
    # Set a variable for the book path
    book_path = "books/frankenstein.txt"
    # Create a method that read the file and store it on a variable
    text = get_book_text(book_path)
    # Using the method get_num_words that count how many words does the file has, we store it on a variable
    num_words = get_num_words(text)
    # Using the method count_letters that count the number of letters and return a dict
    character_count = count_letters(text)
    # Variable that store the dict that we convert into a list
    list = dict_to_sorted_list(character_count)

    print(f"---Begin report of {book_path}")
    print(f"{num_words} words found in the document")
    print()

    for item in list:
        if not item["char"].isalpha():
            continue
        print(f"The {item['char']} character was found {item['num']} times")

    print("---End report---")


def sort_on(d):
    return d["num"]


def dict_to_sorted_list(dict):
    sorted_list = []
    for c in dict:
        sorted_list.append({"char": c, "num": dict[c]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


# Method to count the letters and return a dict
def count_letters(text):
    # Crear un diccionario vacío
    dict = {}
    for character in text:
        letter = character.lower()
        if letter in dict:
            dict[letter] = dict[letter] + 1
        else:
            dict[letter] = 1
    return dict


# Method to count the words number
def get_num_words(text):
    words = text.split()
    return len(words)


# Method to read the book
def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
