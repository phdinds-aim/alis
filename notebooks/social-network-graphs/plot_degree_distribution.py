

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