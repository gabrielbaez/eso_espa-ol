import csv, os, deepl

with open('en.lang.csv',newline='', encoding='utf-8') as inf, open('es.lang.csv', 'w',newline='', encoding='utf-8') as outf:
    reader = csv.reader(inf,delimiter=',', quotechar='"',quoting=csv.QUOTE_ALL)
    writer = csv.writer(outf,delimiter=',', quotechar='"',quoting=csv.QUOTE_ALL)
    for line in reader:
        translation, extra_data = deepl.translate(line[4], target="ES")	
        line[4] = translation
        print(line)
        writer.writerow(line)

