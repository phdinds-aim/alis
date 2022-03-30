def graph_to_edge_matrix(G):
    """Convert a networkx graph into an edge matrix.
    
    Parameters
    ----------
    G : networkx graph
    
    Returns
    -------
    array: edge matrix     
    """
    
    # Initialize edge matrix with zeros
    edge_mat = np.zeros((len(G), len(G)), dtype=int)

    # Loop to set 0 or 1 (diagonal elements are set to 1)
    for node in G:
        for neighbor in G.neighbors(node):
            edge_mat[node][neighbor] = 1
        edge_mat[node][node] = 0

    return edge_mat