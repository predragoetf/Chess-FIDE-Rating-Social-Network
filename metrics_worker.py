import networkx as nx
import community
import numpy as np

def mgtg(G):
    G2 = nx.Graph()
    G2.add_nodes_from(list(G))
    
    for u,v,data in G.edges(data=True):
        if G2.has_edge(u,v):
            G2[u][v]['weight'] += 1
        else:
            G2.add_edge(u, v, weight=1)

    return G2

def calculateMetricsForMonth2(year, month, G, output):
    date = "20" + year + "-" + month + "-01"
    #G = getMonthlyGraph(date)
    N = len(G.nodes)
    M = len(G.edges())
    k = 2 * M / N
    if M==0:
        #print("No matches for "+date)
        output.put((year, month, -1, -1, -1, -1, -1, -1, -1))
    else:
        heterogenity_parameter = sum(map(lambda y: y[1] * y[1], G.degree(G.nodes))) / (2 * M)
        G2 = mgtg(G)
        C = np.mean(list(nx.clustering(G2).values()))
        r = nx.degree_assortativity_coefficient(G2)
        #             r['pearson'] = nx.degree_pearson_correlation_coefficient(G)
        #Q = nx.algorithms.community.greedy_modularity_communities(G2)
        Q1 = community.modularity(community.best_partition(G2), G2)
        #             G3 = buildNonIsolateNetwork(G2)
        #             Q_non_isolate = community.modularity(community.best_partition(G3), G3)
        output.put((year, month, N, M, k, heterogenity_parameter, C, r, Q1))