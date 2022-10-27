import re
from typing import List, Tuple


def find_rhyme_pairs(word_list: List[str]) -> List[Tuple[str, str]]:
    rhyme_pairs: List[Tuple[str, str]] = []

    for idx, word_1 in enumerate(word_list):
        for word_2 in word_list[idx + 1:]:
            word_1_rhyme_end = get_rhyme_part(word_1)
            word_2_rhyme_end = get_rhyme_part(word_2)

            if word_1_rhyme_end == word_2_rhyme_end and word_1 != word_2:
                rhyme_pairs.append((word_1, word_2))
        print(word_1_rhyme_end)

    return rhyme_pairs


def get_rhyme_part(word: str) -> str:
    at_last = False
    had_consonant_after_last = False
    at_next_to_last = False
    for idx, i in enumerate(reversed(word)):
        if i in "aeiouäöü":
            if not at_last and not any([j in "aeiouäöü" for j in word[:-(idx+1)]]):
                return word[-(idx+1):]
            if at_last and had_consonant_after_last:
                at_next_to_last = True
            at_last = True
        elif at_next_to_last:
            return word[-idx:]
        elif at_last and not had_consonant_after_last:
            had_consonant_after_last = True


def main():
    word_list = open("reimerei0.txt", encoding="utf-8").read().splitlines()[:-1]
    print(word_list)
    pairs = find_rhyme_pairs(word_list)
    for pair in pairs:
        print(f"{pair[0]} : {pair[1]}")


if __name__ == '__main__':
    #main()
    print(get_rhyme_part("Schlank"))
