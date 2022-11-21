from typing import List, Tuple, Optional

VOWELS = "aeiouäöü"


def find_rhyme_pairs(word_list: List[str]) -> List[Tuple[str, str]]:
    rhyme_pairs: List[Tuple[str, str]] = []

    for idx, word_1 in enumerate(word_list):
        lower_word_1 = word_1.lower()
        for word_2 in word_list[idx + 1:]:
            lower_word_2 = word_2.lower()
            if lower_word_1.endswith(lower_word_2) or lower_word_2.endswith(lower_word_1):
                continue

            word_1_rhyme_end = get_rhyme_part(lower_word_1)
            word_2_rhyme_end = get_rhyme_part(lower_word_2)

            if word_1_rhyme_end and word_2_rhyme_end and word_1_rhyme_end == word_2_rhyme_end:
                rhyme_pairs.append((word_1, word_2))

    return rhyme_pairs


def get_rhyme_part(word: str) -> Optional[str]:
    """
    This function iterates over the word backwards.
    It searches for the first vowel group,
    then for the second vowel group (there must at least one consonant between vowel groups)
    and returns the part of the word that is from the second vowel group to the end of the word.
    If there is only one vowel group in the whole word, it returns after finding the first vowel group.


    The function return None if any of the following is true:
    - the word is empty
    - the word has no vowel groups
    - the resulting part of the word is less than half the whole word (violates second rule of task)

    :param word: The word to get the rhyme part from
    :return: The rhyme part of the word as string or None if [check list above]
    """
    at_last_vowel_group = False
    between_vowel_groups = False
    at_penultimate_vowel_group = False
    result = None
    for idx, i in enumerate(reversed(word)):
        if is_vowel(i, word):
            if not any([is_vowel(j, word) for j in word[:-(idx + 1)]]):
                result = word[-(idx + 1):]
                break
            if at_last_vowel_group and between_vowel_groups:
                at_penultimate_vowel_group = True
            at_last_vowel_group = True
        elif at_penultimate_vowel_group:
            result = word[-idx:]
            break
        elif at_last_vowel_group and not between_vowel_groups:
            between_vowel_groups = True

    if not result or (len(word) / 2) > len(result):
        return None
    return result


def is_vowel(char: str, word: str) -> bool:
    # If the char is "y" and no other vowel is in the word, "y" is considered a vowel
    if char == "y" and not any(v in word for v in VOWELS):
        return True
    return char in VOWELS


def main():
    with open("reimerei3.txt", encoding="utf-8") as file:
        word_list = file.read().splitlines()
    pairs = find_rhyme_pairs(word_list)

    if not pairs:
        print("Keine Reimpaare gefunden.")
        return

    print("Alle Reimpaare:")
    for pair in pairs:
        print(f"{pair[0]} : {pair[1]}")


if __name__ == '__main__':
    main()
