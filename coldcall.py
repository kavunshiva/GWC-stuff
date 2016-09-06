import csv
import random
with open('GWCblackrock2016studentlist-googleformat.csv') as slist:
    slist_parsed = csv.reader(slist)
    slist_py = []
	
    for row in slist_parsed:
        row_contents = row[1] + ' ' + row[3]
        slist_py.append(row_contents)
rand = random.randint(1,(len(slist_py)-1))
print(slist_py[rand])