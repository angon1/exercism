ALPHABET = "abcdefghijklmnopqrstuvwxyz"

# def check_if_all_letters_used(sentence)
#     alphabet_character_set = set(alphabet)
#     sentence_character_set = set(sentence)
#     return

def is_pangram(sentence):
    return set(sentence.lower()).issuperset(set(ALPHABET))
