from bs4 import BeautifulSoup as BS
from requests_html import HTMLSession
from os import system
from re import sub
system("cls")
del system


print(" fefe's")
koofinder3000 = [
    "  _  ______   ____    ______ _____ _   _ _____  ______ _____    ____   ___   ___   ___  ",
    " | |/ / __ \ / __ \  |  ____|_   _| \ | |  __ \|  ____|  __ \  |___ \ / _ \ / _ \ / _ \ ",
    " | ' / |  | | |  | | | |__    | | |  \| | |  | | |__  | |__) |   __) | | | | | | | | | |",
    " |  <| |  | | |  | | |  __|   | | | . ` | |  | |  __| |  _  /   |__ <| | | | | | | | | |",
    " | . \ |__| | |__| | | |     _| |_| |\  | |__| | |____| | \ \   ___) | |_| | |_| | |_| |",
    " |_|\_\____/ \____/  |_|    |_____|_| \_|_____/|______|_|  \_\ |____/ \___/ \___/ \___/ "
]

for i in koofinder3000:
    print(i)
print("\n")

FILTER = " -'"
BASE_URL = "https://www.kooapp.com/profile/"
SYNONYM_URL = "https://www.synonym.com/synonyms/"
OUTPUT = 'results.txt'


def save(txt):
    with open(OUTPUT, 'w') as file:
        for i in txt:
            file.write(i)
            file.write("\n")
        file.flush()


def clear_title(raw):
    clean = raw.split(">")[1]
    clean = clean.split("<")[0]
    return clean


def clear_list(raw_list):
    clean_list = []
    for raw in raw_list:
        raw = str(raw)
        clean = raw.split(">")[2]
        clean = clean.split("<")[0]
        clean_list.append(clean)
    return clean_list


def check(s, target):
    # checks if the handle is taken
    content = s.get(BASE_URL + target).content
    soup = BS(content, 'html.parser')
    title = soup.find_all("title")[0]
    title = str(title)
    title = clear_title(title)
    if title == "Invalid Profile - Koo":
        print(f"{target} may not be taken")
        return False
    print(f"{target} is taken")
    return True


def get_synonym(s, target):
    # gets synonyms
    content = s.get(SYNONYM_URL + target).content
    soup = BS(content, 'html.parser')
    synonyms = soup.find("div", {"data-section": "synonyms"})
    synonyms = synonyms.findChildren("li", {"class": "chip"})
    synonyms = clear_list(synonyms)
    exclude = []
    for sy in synonyms:
        for char in sy:
            if char in FILTER:  
                exclude.append(sy)
    for ex in exclude:
        try:
            synonyms.remove(ex)
        except:
            ...
    return synonyms


with HTMLSession() as s:
    try:
        target = input("[@]: ")
        if not check(s, target):
            print("handle is avaliable!!!!!!")
        else:
            print("checking for synonyms...")
            synonyms = get_synonym(s, target)
            for sy in synonyms:
                check(s, sy)
    except:
        print("FALHAAAA ERROR FATTAL!!!")
