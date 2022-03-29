# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 23:35:46 2022

@author: Ranzivelle
"""
import networkx as nx

def draw_true_vs_pred(G, y_true, y_pred, pos,):
    
    for i in range(len(y_true)):
        if y_pred is not None:
            if y_true[i] == y_pred[i]:
                node_color = [0, 1, 0]
                node_shape = 'o'
            else:
                node_color = [0, 0, 0]
                node_shape = 'X'
                
        nx.draw_networkx_nodes(G, pos,
#                               nodelist=[student],
                               node_color=node_color,
                               node_size=250,
                               alpha=0.7,
#                               ax=ax,
                               node_shape=node_shape)
    
    # Draw edges and show final plot
#    ax.set_title(algo_name)
    nx.draw_networkx_edges(G, pos, alpha=0.5)