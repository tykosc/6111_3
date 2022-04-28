# assumptions:
# 1/ the input file is in the same directory as the script or in the ./datasets directory
# 2/ the input file is a csv file
# 3/ the input file has no headers
# 4/ each row of the input file is a comma separated list of items

# imports
import sys
import csv
import numpy as np

from apriori import AprioriBase

filename = sys.argv[1]
min_sup = float(sys.argv[2])
min_conf = float(sys.argv[3])

file = None
try:
    file = open(filename, 'r', newline='')
except FileNotFoundError:
    # try to open the file in the ./datasets directory
    try:
        file = open('./datasets/' + filename, 'r', newline='')
    except FileNotFoundError:
        print('File not found')
        exit(1)

reader = csv.reader(file)
frequent_itemsets = AprioriBase(list(reader), min_sup, min_conf)
frequent_itemsets.run()
frequent_itemsets.pprint_association_rules(frequent_itemsets.generate_association_rules())

