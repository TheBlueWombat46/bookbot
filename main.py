def main():
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_list = get_word_list(book_text)
    character_count = get_character_count(book_text)
    letter_printout(book_path, alphabet)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_list(text):
    words = text.split()
    return words

def get_word_count(text_list):
    return len(text_list)

def get_character_count(text):
    characters = {}

    for character in text:
        character = character.lower()
        if(character in characters):
            characters[character] += 1
        else:
            characters[character] = 1

    return characters

def letter_printout(book_path, character_list):
    text = get_book_text(book_path)
    characters = get_character_count(text)
    word_count = get_word_count(get_word_list(text))

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print("")

    for letter in character_list:
        if letter in characters:
            print(f"The '{letter}' character was found {characters[letter]} times")

    print("--- End report ---")

main()