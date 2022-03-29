# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 10:14:48 2022

@author: Ranzivelle
"""

import networkx as nx

def closeness_centrality(G):
    """Calculates the closeness centrality of each node in a graph 
    Parameters
    
    G : networkx graph
    
    Returns
    -------
    sorted list of degree centrality values of each node 
    """ 
    print("closeness centrality:")
    for k, v in sorted(nx.closeness_centrality(G).items(), key=lambda x: -x[1]):
        print(str(k)+":"+"{:.3}".format(v)+" ", end="")
    print("\n")