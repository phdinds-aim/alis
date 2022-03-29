# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 11:37:45 2022

@author: Ranzivelle
"""
import numpy as np

def graph_to_edge_matrix(G):
    """Convert a networkx graph into an edge matrix.
    
    Parameters
    ----------
    G : networkx graph
    """
    # Initialize edge matrix with zeros
    edge_mat = np.zeros((len(G), len(G)), dtype=int)

    # Loop to set 0 or 1 (diagonal elements are set to 1)
    for node in G:
        for neighbor in G.neighbors(node):
            edge_mat[node][neighbor] = 1
        edge_mat[node][node] = 0

    return edge_mat