"""
MVP of the ryming product.

Takes in two words and finds the words that ryhme
"""

import requests
import sys
import fileinput

word_1 = 'shirt'
word_2 = 'histogram'

def _main():
    rhymes_1 = rhyme_words(word_1)
    rhymes_2 = rhyme_words(word_2)
    print(rhymes_2)
    print(rhymes_1)
    if len(rhymes_1) < 0 or len(rhymes_2) < 0:
        assert ValueError("One word has no rymes")
    valid_rhymes = []
    for r1 in rhymes_1:
        for r2 in rhymes_2:
            if r2 in r1:
                valid_rhymes.append((r1, r2))
            print(r1, r2)
    print("Valid Rhmes are:".format(valid_rhymes))


def phoneme_dictionary():
    """
    Loads the dictionary of phonemes and returns a dict

    :return: dict of form {word: phonemes}
    """
    r = requests.get('https://svn.code.sf.net/p/cmusphinx/code/trunk/cmudict/cmudict.0.7a')
    phoneme_raw = r.text.splitlines()
    phoneme_raw = phoneme_raw[54:]
    phoneme_dict = {}
    for line in phoneme_raw:
        separate = line.find(" ")
        word = line[:separate]
        phoneme = line[separate+2:]
        phoneme_dict[word] = phoneme
    return phoneme_dict

phoneme_dict = phoneme_dictionary()


def rhyme_words(word):
    """
    Finds the ryhming words of word
    :param word: str
    :return: list of rhyme words
    """
    word_uc = word.upper()
    rhyme_list = []
    for key, phoneme in phoneme_dict.items():
        if key != word_uc:
            if phoneme.split()[-2:] == phoneme_dict[word_uc].split()[-2:]:
                rhyme_list.append(key)
    return rhyme_list


if __name__ == '__main__':
    sys.exit(_main())