def main():
    file_path = "books/frankenstein.txt"
    with open(file_path) as f:
        file_contents = f.read()
#        print_book(file_contents)
#        print(get_word_count(file_contents))
#        print(get_character_dict(file_contents.lower()))
        char_dict = get_character_dict(file_contents.lower())
        my_list = get_descended_char_counts(char_dict)
        print_report(file_path, file_contents, my_list)

def print_book(s):
    print(s)

def get_word_count(s):
    return len(s.split())

def get_character_dict(s):
    characters = {}
    for c in s:
        if c in characters:
            characters[c] = characters[c] + 1
        else:
            characters[c] = 1
    return characters

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["num"]

def get_descended_char_counts(d):
    list_dict = []
    for k in d.keys():
        if k.isalpha():
            list_dict.append({"name":k,"num":d[k]})
    list_dict.sort(reverse=True, key=sort_on)
    return list_dict

def print_report(file_path, file_contents, sorted_list):
    print_report_start(file_path)
    print_word_count(file_contents)
    print()
    print_sorted_character_counts(sorted_list)
    print_end_report()

def print_report_start(file_path):
    print(f"--- Begin report of {file_path} ---")

def print_word_count(file_contents):
    print(f"{get_word_count(file_contents)} words found in the document")

def print_sorted_character_counts(sorted_list):
    for dict in sorted_list:
        print(f"The '{dict['name']}' character was found {dict['num']} times")

def print_end_report():
    print("--- End report ---")

main()
