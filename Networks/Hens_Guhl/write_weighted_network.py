import networkx as nx

G= nx.read_edgelist("hens_pecking_order_PS.edgelist", nodetype = int)

print nx.info(G)

nx.write_graphml(G, "weighted_hens_pecking_order.graphml")
