import sys

import requests as re
from bs4 import BeautifulSoup
def scraping_translations(soup):

    translations = soup.find_all('a', class_='translation')
    translations_list = []

    for p in translations:
        translations_list.append(p.text.strip())

    return translations_list
def scraping_examples(soup):

    examples = soup.find_all('div', class_='example')
    examples_list = []

    for e in examples:
        examples_list.append(e.text.strip().replace("\n","").replace("\r","").replace("          ", "\n"))

    return examples_list


def displaying_and_saving(translations_list, examples_list, name, targ_language):
    with open(f"{name}.txt", "a", encoding="utf-8") as f:
        print(targ_language, "Translations:")
        f.write(f"{targ_language} Translations:\n")
        for i in translations_list:
            print(i)
            f.write(i + "\n")
        print(targ_language, "Examples:\n")
        f.write(f"{targ_language} Examples:\n\n")
        for i in examples_list:
            print(i)
            print()
            f.write(i)
            f.write("\n\n")
        f.write("\n")
        print()

class LanguageSupportError(Exception):
    def __str__(self):
        return "Sorry, the program doesn't support"

def language_checker(a):
    try:
        if a not in languages:
            raise LanguageSupportError
    except LanguageSupportError as err:
        print(err, a)

def procedure(targ_language):
    soup = BeautifulSoup(r.content, "html.parser")
    translation_list = scraping_translations(soup)
    examples_list = scraping_examples(soup)
    displaying_and_saving(translation_list, examples_list, word, targ_language)

class StatusCodeError(Exception):
    def __init__(self, text):
        self.message = text
        super().__init__(self.message)

def connection_checker(r, word):
    if r.status_code == 404:
        print(f"Sorry, unable to find {word}")
        sys.exit()

headers = {'User-Agent': 'Mozilla/5.0'}
languages = ["arabic", "german", "english", "spanish", "french", "hebrew", "japanese", "dutch", "polish", "portuguese", "romanian", "russian", "turkish", "all"]


curr_language = sys.argv[1]
language_checker(curr_language)
targ_language = sys.argv[2]
language_checker(targ_language)

word = sys.argv[3]

if targ_language == "all":
    for i in languages:
        r = re.get(f"https://context.reverso.net/translation/{curr_language.lower()}-{i.lower()}/{word}", headers=headers)
        connection_checker(r, word)
        procedure(i)
else:
    r = re.get(f"https://context.reverso.net/translation/{curr_language.lower()}-{targ_language.lower()}/{word}", headers=headers)
    connection_checker(r, word)
    procedure(targ_language)
