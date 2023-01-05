"""https://graphviz.org/Gallery/directed/cluster.html"""

from graphviz import Digraph

g = Digraph('G', filename='cluster.gv')

# NOTE: the subgraph name needs to begin with 'cluster' (all lowercase)
#       so that Graphviz recognizes it as a special cluster subgraph

with g.subgraph(name='cluster_0') as c:
    c.attr(style='filled', color='lightgrey')
    c.node_attr.update(style='filled', color='white')
    c.edges([('a0', 'a1')])
    c.attr(label='process #1')

with g.subgraph(name='cluster_1') as c:
    c.attr(style='filled', color='lightgrey')
    c.node_attr.update(style='filled', color='white')
    c.edges([('b0', 'b1')])
    c.attr(label='process #1')

g.edge('start', 'a0')
g.edge('start', 'b0')

g.node('start', shape='Mdiamond')
g.node('end', shape='Msquare')

g.view()