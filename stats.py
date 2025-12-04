def string_to_words(text): 
    words = text.split()
    print("----------- Word Count ----------")
    print(f"Found {len(words)} total words.")
    return words


def create_character_frequency_dict(text):
    print("--------- Character Count -------")
    freq_dict = {}
    for char in text:
        char = char.lower()
        if not char.isalpha():
            continue
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    return freq_dict


def sort_freq_dict(freq_dict):
    dict_list = []
    for key in freq_dict:
        dict_list.append({"char": key, "num": freq_dict[key]})
    
    return order_dict(dict_list)

def order_dict(dict_list):
    dict_list.sort(key=lambda x: x["num"], reverse=True)
    return dict_list


def print_format_list(dict_list):
    for item in dict_list:
        print(f"{item['char']}: {item['num']}")

def analyze_book_stats(text):
    string_to_words(text)
    char_freq = create_character_frequency_dict(text)
    sorted_char_freq = sort_freq_dict(char_freq)
    print_format_list(sorted_char_freq)