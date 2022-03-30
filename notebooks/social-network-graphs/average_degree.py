
import matplotlib.pyplot as plt


def average_degree(G):
    """Calculates the average degree of a graph 
    Parameters
    
    G : networkx graph
    
    Returns
    -------
    float
    average degree of a graph  
    """ 
    degree = G.degree()

    degree_list = []

    for (n,d) in degree:
        degree_list.append(d)

    av_degree = sum(degree_list) / len(degree_list)

    return av_degree
