def main():
# open the frankenstein.txt file in the books directory
    file_path = "books/frankenstein.txt"
    with open(file_path) as f:
        file_contents = f.read()

    # print("The text has been successfully read")

    # count the number of words in the file and print it
    word_count = count_words(file_contents)
    # print(f"The number of words in Frankenstein: {word_count}")

    # count the occurences of each character and print it
    char_count = count_characters(file_contents)
    # print(f"Character counts: {char_count}")

    # print final report
    print_report(file_path, word_count, char_count )

def count_words(text):
    # split the text into words by whitespace and return the length of the resulting list
    words = text.split()
    return len(words)

def count_characters(text):
    # convert the text to lowercase to avoid duplicates
    text = text.lower()

    # create an empty dictionary to hold the count of each character
    char_count = {}

    for char in text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    return char_count

def get_character_count(character_tuple):
    # this function returns the count of the character from the tuple
    return character_tuple[1]

def print_report(file_path, word_count, char_count):
    # print the report header
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document\n")

    # convert the char_count dictionary to a list of tuples (character, count)
    char_count_list = list(char_count.items())

    # sort the list of tuples by the count in descending order
    char_count_list.sort(key=get_character_count, reverse=True)

    # print the sorted characters and their counts
    for char, count in char_count_list:
        print(f"The '{char}' character was found {count} times")

    # print the report footer
    print("--- End report ---")

main()