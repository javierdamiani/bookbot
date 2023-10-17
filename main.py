with open("./books/frankenstein.txt") as f:
    file_content = f.read()
    text_str = str(file_content)
    words = text_str.split()
    len = len(words)
    print(len)
