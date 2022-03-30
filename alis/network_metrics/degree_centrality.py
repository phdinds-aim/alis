def degree_centrality(G):
    """Calculates the degree centrality of each node in a graph 
    
    Parameters
    -------
    G : networkx graph
    
    Returns
    -------
    sorted list of degree centrality values of each node 
    """ 
    for k, v in sorted(nx.degree_centrality(G).items(), key=lambda x: -x[1]):
        print(str(k)+":"+"{:.3}".format(v)+" ", end="")
    print("\n")