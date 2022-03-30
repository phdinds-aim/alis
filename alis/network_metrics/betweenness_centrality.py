def betweenness_centrality(G):
    """Calculates the betweenness centrality of each node in a graph 
    
    Parameters
    -------
    G : networkx graph
    
    Returns
    -------
    sorted list of degree centrality values of each node 
    """ 
    
    print("betweenness centrality:")
    for k, v in sorted(nx.betweenness_centrality(G).items(), key=lambda x: -x[1]):
        print(str(k)+":"+"{:.3}".format(v)+" ", end="")
    print("\n")