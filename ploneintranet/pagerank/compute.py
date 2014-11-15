import networkx as nx
from ploneintranet.pagerank.graph import Graphs


class Compute(object):
    """Compute PageRank per node on the object/user/tag/etc graph."""

    def __init__(self):
        self.graphs = Graphs()

    def pagerank(self, edge_weights={}, context=None, context_weight=10):
        G = self.graphs.unify_weighted(edge_weights)
        if not context:
            return nx.pagerank(G)
        else:
            weights = {}
            for k in G.nodes():
                weights[k] = 1
            weights[context] = context_weight
            return nx.pagerank(G, personalization=weights)
