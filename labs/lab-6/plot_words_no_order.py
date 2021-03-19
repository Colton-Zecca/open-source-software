"""
=====
Words
=====

Words/Ladder Graph
------------------
Generate  an undirected graph over the 5757 5-letter words in the
datafile `words_dat.txt.gz`.  Two words are connected by an edge
if they differ in one letter, resulting in 14,135 edges. This example
is described in Section 1.1 in Knuth's book (see [1]_ and [2]_).

References
----------
.. [1] Donald E. Knuth,
   "The Stanford GraphBase: A Platform for Combinatorial Computing",
   ACM Press, New York, 1993.
   [2] http://www-cs-faculty.stanford.edu/~knuth/sgb.html
.. [3] Aric Hagberg, Brendt Wohlberg, See: https://github.com/rcos/networkx/blob/master/examples/graph/plot_words.py
"""
#    BSD license. See reference [3]

import gzip
from string import ascii_lowercase as lowercase

import networkx as nx
from itertools import permutations

# Words is a list of every word in the dataset
def generate_graph(words):
    G = nx.Graph(name="words")
    # Lowercase is the set of all lowercase characters a-z
    # Lookup is a dictionary where: key (lowercase character) --> value (index in alphabet [0-indexed])
    lookup = dict((c, lowercase.index(c)) for c in lowercase)
    
    # Change one letter, don't care about the order
    def edit_distance_one(word):
        for permuted_word in list(map(''.join, permutations(word))): #Generate a list of every single possible permutation of this word
            for i in range(len(permuted_word)):
                left, c, right = permuted_word[0:i], permuted_word[i], permuted_word[i + 1:]
                j = lookup[c]  # lowercase.index(c)
                for cc in lowercase[j + 1:]:
                    yield left + cc + right


    candgen = ((word, cand) for word in sorted(words)
               for cand in edit_distance_one(word) if cand in words)
            #    Sort of all the words, and for each word, change 
    
    G.add_nodes_from(words)
    for word, cand in candgen:
        G.add_edge(word, cand)
    return G


def words_graph():
    """Return the words example graph from the Stanford GraphBase"""
    fh = gzip.open('words_dat.txt.gz', 'r')
    words = set()
    for line in fh.readlines():
        line = line.decode()
        if line.startswith('*'):
            continue
        w = str(line[0:5])
        words.add(w)
    return generate_graph(words)


if __name__ == '__main__':
    G = words_graph()
    print("Loaded words_dat.txt containing 5757 five-letter English words.")
    print("Two words are connected if they differ in one letter.")
    print("Graph has %d nodes with %d edges"
          % (nx.number_of_nodes(G), nx.number_of_edges(G)))
    print("%d connected components" % nx.number_connected_components(G))

    for (source, target) in [('chaos', 'order'),
                             ('nodes', 'graph'),
                             ('moron', 'smart'),
                             ('flies', 'swims'),
                             ('mango', 'peach'),
                             ('pound', 'marks')]:
        print("Shortest path between %s and %s is" % (source, target))
        try:
            sp = nx.shortest_path(G, source, target)
            for n in sp:
                print(n)
        except nx.NetworkXNoPath:
            print("None")
