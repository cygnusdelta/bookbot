def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    characters = character_count(text)
    total_words = word_count(text)
    sorted_count = sort(characters)
    report(book_path, total_words, sorted_count)

##counts the number of each character (ignoring case) and returns a
# dictionary in letter : number pairs
 
def character_count(text):
    character_dict = {}
    for char in text:
        lowered_char = char.lower()
        if lowered_char.isalpha() == True:
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

#returns the "num" key for .sort

def sort_on(dict):
    return dict["num"]

#sorts the character_count as two key pairs and arranges them by most
#to least common

def sort(dict):
    dict_list = []
    for k in dict:
        item = {"character" : k, "num" : dict[k]}
        dict_list.append(item)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

#formats and prints the report

def report(book_path, total_words, sorted_count):
    print(f"""--- Begin report of {book_path} ---
{total_words} words found in document
          
""")
    for i in sorted_count:
        character = i["character"]
        number = i["num"]
        print(f"The {character} character was found {number} times")
    print("--- End Report ---")
    return
main()
