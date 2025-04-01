def word_count(text):
    count = len(text.split())
    return count

def character_count(text):
    letter_counts = {}
    text = text.lower()
    for character in text:
        if character in letter_counts:
            letter_counts[character] += 1
        else:
            letter_counts[character] = 1
    return letter_counts

def sort_on(d):
    return d["num"]


def sorted_list(num_chars_dict):
    new_list = []
    for ch in num_chars_dict:
        new_list.append({"char": ch, "num": num_chars_dict[ch]})
    new_list.sort(reverse=True, key=sort_on)
    return new_list