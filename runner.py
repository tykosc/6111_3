# assumptions:
# 1/ the input file is in the same directory as the script or in the ./datasets directory
# 2/ the input file is a csv file
# 3/ the input file has no headers
# 4/ each row of the input file is a comma separated list of items

# imports
import sys
import csv
import numpy as np

from apriori import Apriori

filename = sys.argv[1]
min_sup = sys.argv[2]
min_conf = sys.argv[3]

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

# TODO : insert pre-processing hooks here if the CSV needs
# to be pre-processed
reader = csv.reader(file)

frequent_itemsets = Apriori(list(reader), min_sup, min_conf)

