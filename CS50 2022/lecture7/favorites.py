import csv


langs = {}

with open('favorites.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row['language'] in langs:
            langs[row['language']] += 1
        else:
            langs[row['language']] = 1

# for lang in sorted(langs, key=lambda lang: langs[lang], reverse=True):
    # print(f'{lang}: {langs[lang]}')

fav = input('Favorite language: ')
fav = fav.title()
if fav in langs:
    print(f'{fav}: {langs[fav]}')
else:
    print('Invalid language')
