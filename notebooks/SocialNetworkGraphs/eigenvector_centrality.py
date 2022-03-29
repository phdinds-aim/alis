# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 10:14:48 2022

@author: Ranzivelle
"""

import networkx as nx

def eigenvector_centrality(G):
    """Calculates the eigenvector centrality of each node in a graph 
    Parameters
    
    G : networkx graph
    
    Returns
    -------
    sorted list of degree centrality values of each node 
    """ 
    print("eigenvector centrality:")
    for k, v in sorted(nx.eigenvector_centrality(G).items(), key=lambda x: -x[1]):
        print(str(k)+":"+"{:.3}".format(v)+" ", end="")
    print("\n")