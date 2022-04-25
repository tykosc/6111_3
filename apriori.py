# classes for all implementations of apriori algorithm

import csv
from email.policy import default
import pandas as pd
from pandasql import sqldf
import itertools

from collections import defaultdict
from collections import OrderedDict

class Apriori:
    '''
    abstract class for apriori algorithm
    does not implement the algorithm but does
    everything else required for the algorithm
    '''

    def __init__(self, d, min_sup, min_conf) -> None:
        # the set of all transactions
        self.d = d

        self.min_sup = min_sup
        self.min_conf = min_conf

        # a dictionary of the form
        # <k, p>; where p is a dict of form
        # p = < i, c >; i = (item, ) c = count
        # p is a collection of large k-itemsets
        # i represents a tuple of items (in sorted order)
        self.freq = {0:{}}

        # generate frequent 1-itemsets along with trie representations
        self.freq[1]= self.get_f1_items()

    def get_f1_items(self) -> dict:

        counts = defaultdict(int)

        for txn in self.d:
            for item in txn:
                counts[(item, )] += 1

        # TODO : Check if this is the right way to do it.
        # per Ullman lec - there should be only one pass on the dataset.
        counts = { x : (y /len(self.d))  for x, y in counts.items() if (y / len(self.d)) >= self.min_sup }
        counts = OrderedDict(sorted(counts.items(), key = lambda t: t[0]))
        return counts

    def run(self) -> None:
        '''
        Main Apriori Algorithm
        '''
        raise NotImplementedError

    def apriori_gen(self, k) -> None:
        '''
        k-frequent itemset generator function
        '''
        raise NotImplementedError



class AprioriBase(Apriori):
    '''
    Implement Classic Apriori Algorithm
    Fig. 1 - Fast Algorithms for Mining Association Rules in Large Databases, VLDB 1994
    '''

    def __init__(self, d, min_sup, min_conf) -> None:
        super().__init__(d, min_sup, min_conf)

    def run(self):

        k = 2
        while len(self.freq[k - 1]) > 0:
            candidates = self.apriori_gen(k)
            k -= 1

    def apriori_gen(self, k) -> None:
        '''
        here if k = 1 -> l = {}
        '''
        l = {}
        l = self.freq[k - 1]
        l = pd.DataFrame(list(l.keys()), columns=[f'c{k}' for k in list(range(1,k))])

        c_k = []

        query = 'SELECT '
        for i in range(1,k):
            query += f'l1.c{i},'
        query = query[:-1]
        query += f',l2.c{k-1}'
        query += ' FROM l l1, l l2 WHERE '
        for i in range(1,k-1):
            query += f'l1.c{i} = l2.c{i} AND '
        query += f'l1.c{k-1} < l2.c{k-1}'
        q = sqldf(query)

        for _, row in q.iterrows():
            r = list(itertools.combinations(row,k - 1))
            rowflag = False
            for combination in r:
                if combination not in self.freq[k-1]:
                    rowflag = True
            if not rowflag:
                c_k.append(tuple(row))

        print(c_k)
        return list(c_k)

if __name__ == '__main__':

    file = open('./datasets/test_dataset.csv', 'r', newline='')
    file = csv.reader(file)
    abs = AprioriBase(list(file), 0.4, 0.4)

    # run python in interactve mode
    # python -i apriori.py
    # >>> abs.freq