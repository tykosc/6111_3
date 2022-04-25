# classes for all implementations of apriori algorithm
# 
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
            C_k = self.apriori_gen(k) # new candidates, this is a LIST of sets
            C_k_dict = defaultdict(int, {tuple(k): 0 for k in C_k}) # dictionary with tuples as keys  
            for t in self.d:
                # C_t is a list that contains all items of C_k that are subsets of t
                C_t = []
                t = set(t)
                for s in C_k: 
                    if set(s).issubset(t):
                        C_t.append(s)
                for c in C_t: 
                    tup = tuple(c)
                    C_k_dict[tup] += 1
            
            for key in C_k_dict.copy():
                C_k_dict[key] = C_k_dict[key]/len(self.d)
                if C_k_dict[key] < self.min_sup:
                    del C_k_dict[key]
            
            self.freq[k] = C_k_dict
            k += 1
        print(self.freq)
    
    def generate_association_rules(self):
        high_confidence_rules = {} # dictionary where the key is a tuple representing an association rule and val is a dictionary {'sup': 'conf': }
        k = 2
        while self.freq[k]: # while there exists large itemsets of size k
            d = self.freq[k]
            d_lhs = self.freq[1]
            for key,val in d.items():
                # generate all permutations of keys - permutation ('a', 'b', 'c') represents 'a' -> 'b', 'c'
                perms = list(itertools.permutations(key))
                print(perms)
                for p in perms: 
                # Calculate the confidence: supp(LUR)/supp(L) = v / d_lhs[p[0]]]
                    print(p)
                    print(type(p))
                    conf = val / d_lhs[(p[0], )]
                    if conf >= self.min_conf:
                        # if confidence is high, add it to high confidence association rules
                        high_confidence_rules[p] = {'sup': val, 'conf': conf}
            k += 1
        return high_confidence_rules

    
    def pprint_association_rules(self, rules):
        for key, value in rules.items():
            l = list(key)
            lhs = [l[0]]
            rhs = l[1:]
            conf = f"{value['conf']:.0%}"
            sup = f"{value['sup']:.0%}"
            print(f'{lhs} ==> {rhs} (Conf: {conf}, Supp: {sup})')


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
    abs.run()
    abs.pprint_association_rules(abs.generate_association_rules())



    # run python in interactve mode
    # python -i apriori.py
    # >>> abs.freq
    