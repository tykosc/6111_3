# classes for all implementations of apriori algorithm

import csv
from email.policy import default
import numpy as np

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
        self.freq = defaultdict()

        # a map of trie data structures to enable fast joins
        self.ftries = defaultdict()
        
        # generate frequent 1-itemsets along with trie representations
        self.freq[1], self.ftries[1] = self.get_f1_items()

    def get_f1_items(self) -> dict:

        counts = defaultdict(int)

        for txn in self.d:
            for item in txn:
                counts[(item, )] += 1

        # TODO : Check if this is the right way to do it.
        # per Ullman lec - there should be only one pass on the dataset.
        counts = { x : y for x, y in counts.items if y >= self.min_sup }
        counts = OrderedDict(sorted(counts, key = lambda t: t[0]))
        return counts, counts

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
            candidates = self.apriori_gen(k-1)
        for 



if __name__ == '__main__':

    file = open('./datasets/test_dataset.csv', 'r', newline='')
    file = csv.reader(file)
    abs = Apriori(file, 0.1, 0.2)

    # run python in interactve mode
    # python -i apriori.py
    # >>> abs.freq