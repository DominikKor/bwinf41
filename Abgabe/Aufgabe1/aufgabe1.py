def find_all(search_term: str, text: str):
    text = text.split()
    terms = search_term.split()
    result = []
    for idx, word in enumerate(text):
        if get_lower_letters_only(word) == get_lower_letters_only(terms[0]) or terms[0] == "_":
            found_passage = True
            for idx2, term in enumerate(terms):
                if term == "_":
                    continue
                try:
                    is_match = get_lower_letters_only(term) == get_lower_letters_only(text[idx + idx2])
                except IndexError:
                    found_passage = False
                    break
                if not is_match:
                    found_passage = False
                    break
            if found_passage:
                result.append(" ".join(text[idx:idx + (len(terms))]))
    return result


def get_lower_letters_only(word: str):
    return "".join([letter for letter in word if letter.isalnum()]).lower()


def main():
    with open("Alice_im_Wunderland.txt", encoding="utf-8-sig") as file:
        book_text = file.read()

    with open("stoerung0.txt", encoding="utf-8") as file:
        search_term = file.read().strip()
        if not search_term:
            print("Die Eingabe ist leer. Bitte überprüfen Sie die Eingabedatei.")
            return

    results = find_all(search_term, book_text)

    if not results:
        print("Es wurde keine passende Passage gefunden.")
        return

    print("Alle gefundenen Passagen:")
    for result in results:
        print(result)


if __name__ == "__main__":
    main()
