# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 10:14:48 2022

@author: Ranzivelle
"""

#import networkx as nx
import matplotlib.pyplot as plt


def plot_degree_distribution(G):
    """Plots the degree distribution of a graph 
    Parameters
    
    G : networkx graph
    
    Returns
    -------
    degree distribution plot 
    """ 
    degree = G.degree()

    degree_list = []

    for (n,d) in degree:
        degree_list.append(d)

    av_degree = sum(degree_list) / len(degree_list)


    plt.hist(degree_list,label='Degree Distribution')
    plt.axvline(av_degree,color='r',linestyle='dashed',label='Average Degree')  
    plt.legend()
    plt.ylabel('Number of Nodes')