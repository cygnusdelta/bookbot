def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    characters = character_count(text)
    total_words = word_count(text)

    print(characters)

##counts the number of each character (ignoring case) and returns a
# dictionary in letter : number pairs
 
def character_count(text):
    character_dict = {}
    for char in text:
        lowered_char = char.lower()
        if lowered_char not in character_dict:
            character_dict[lowered_char] = 1
        else:
            character_dict[lowered_char] += 1
    return character_dict

#counts the number of words in a given string

def word_count(text):
    words = text.split()
    return len(words)

#returns text of a book

def get_book_text(path):
    with open(path) as f:
        return f.read()
main()
