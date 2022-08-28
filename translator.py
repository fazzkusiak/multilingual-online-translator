import sys

import requests as re
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0'}
print("Hello, welcome to the translator. Translator supports:")

languages = ["Arabic", "German", "English", "Spanish", "French", "Hebrew", "Japanese", "Dutch", "Polish", "Portuguese", "Romanian", "Russian", "Turkish"]
for i, j in enumerate(languages):
    print(i, ".", j, sep=None)
curr_number_language = int(input('Type the number of your language'))
curr_language = languages[curr_number_language - 1]

targ_number_language = int(input("Type the number of language you want to translate to: "))
targ_language = languages[targ_number_language - 1]

word = input("Type the word you want to translate:")
r = re.get(f"https://context.reverso.net/translation/{curr_language.lower()}-{targ_language.lower()}/{word}", headers=headers)
if r:

    print('200 OK\n')

    soup = BeautifulSoup(r.content, "html.parser")
    translations = soup.find_all('a', class_='translation')
    translations_list = []
    examples = soup.find_all('div', class_='example')
    examples_list = []
    for p in translations:
        translations_list.append(p.text.replace("m", "").strip())

    for e in examples:
        examples_list.append(e.text.strip().replace("\n","").replace("\r","").replace("          ", "\n"))

    print(targ_language, "Translations:")
    for i in translations_list:
        print(i)
    print(targ_language, "Examples:")
    for i in examples_list:
        print(i)
        print()

