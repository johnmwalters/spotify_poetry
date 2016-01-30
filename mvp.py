"""
MVP of the ryming product.

Takes in two words and finds the words that ryhme
"""

import requests
import sys
import itertools
from PyDictionary import PyDictionary

dictionary=PyDictionary()



word_1 = 'shirt'
word_2 = 'dress'

def _main():
    synonyms_1 = synonyms(word_1) + [word_1]
    synonyms_2 = synonyms(word_2) + [word_2]


    valid_rhymes = []

    print(rhyme_words(word_1))
    print('skirt' in rhyme_words(word_1))
    for i in rhyme_words(word_1):  # Skirt should be in i
        if i in synonyms_2:
            print(word_1, i)


def synonyms(word):
    synonym_list = dictionary.synonym(word)
    return synonym_list


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
            try:
                if phoneme.split()[-2:] == phoneme_dict[word_uc].split()[-2:]:
                    rhyme_list.append(key)
            except KeyError:
                print("{} not found".format(key))
                continue
    return rhyme_list


if __name__ == '__main__':
    sys.exit(_main())