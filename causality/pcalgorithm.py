"""
Peter Spirtes, Clark Glymour, and Richard Scheines developed an account of causal discovery in the 
last decade of the twentieth century. Their approach was to induce a partially directed causal graph 
from independence constraints embodied in a database of past case data. Undirected edges in this graph 
indicate causal relations of unknown direction. They developed the PC algorithm (named after its authors, 
Peter and Clark) to construct the graph:

1. Start off with a complete undirected graph on V.
2. For n=0,1,2,...remove any edges A − B if (A⊥B|X) for some set X of n neighbors of A.
3. For each structure A − B − C in the graph with A and C not adjacent, substitute A -> B <- C 
    if B was not found to screen off A and C in the previous step.
4. Repeatedly substitute
    (i) A -> B -> C for A -> B − C with A and C non-adjacent. 
    (ii) A -> B for A - B if there is a chain of arrows from A to B.
"""

def depend(a, b, x):
    """
    For some edge a - b, if there is a conditional dependence on x, return True.
    Otherwise return False.
    """
    if x in list(a, b):
        return True
    return False  

def pcalg(g, n):
    """
    For some undirected graph g (dictionary with keys as nodes and values as a list of the nodes 
    which the nodes connect to) on V with number of neighbors n, we use the PC algorithm 
    to induce a partially directed causal graph from independence constraints embodied
    in a database of past case data.
    """
    # step 2. remove edges without the conditional dependence
    for i in range(n+1): # as described by step 2 above.
        for j in g: # for each key (node) in the dictionary g
            for k in g[j]: # for each value (connecting edge to the node) in the key j
                if depend(j, k, i):
                    g[j].remove(k) 
    gn = {} # new graph gn with directed edges          
    for A in g: # for each key (node) in the dictionary g
        for B in g[A]: # for each connecting node
            if g[B]: 
                for C in g[B]:
                    if k not in g[A]: # if C is not adjacent to A
                        if not gn[A]: # add A -> B to our new dictionary gn
  		            gn[A] = [B]
 		        else:
                            gn[A].append(B)
                        if not gn[C]: # add C -> B
                            gn[C] = [B]
                        else:
                            gn[C].append(B)
    return gn
