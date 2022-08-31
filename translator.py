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

def procedure(targ_language):
    soup = BeautifulSoup(r.content, "html.parser")
    translation_list = scraping_translations(soup)
    examples_list = scraping_examples(soup)
    displaying_and_saving(translation_list, examples_list, word, targ_language)

headers = {'User-Agent': 'Mozilla/5.0'}
print("Hello, welcome to the translator. Translator supports:")

languages = ["Arabic", "German", "English", "Spanish", "French", "Hebrew", "Japanese", "Dutch", "Polish", "Portuguese", "Romanian", "Russian", "Turkish"]
for i, j in enumerate(languages):
    print(i, ".", j, sep=None)
curr_number_language = int(input('Type the number of your language: '))
curr_language = languages[curr_number_language - 1]

targ_number_language = int(input("Type the number of a language you want to translate to or '0' to translate to all languages:"))

word = input("Type the word you want to translate:")
if targ_number_language == 0:
    for i in languages:
        r = re.get(f"https://context.reverso.net/translation/{curr_language.lower()}-{i.lower()}/{word}", headers=headers)
        procedure(i)
else:
    targ_language = languages[targ_number_language - 1]
    r = re.get(f"https://context.reverso.net/translation/{curr_language.lower()}-{targ_language.lower()}/{word}", headers=headers)
    procedure(targ_language)
