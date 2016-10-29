from ClusterShell.NodeSet import NodeSet, RangeSet
from ClusterShell.Task import task_self
import sys
# Constructeurs
node0 = NodeSet()

i=0
nbNoeud = len(sys.argv)-2
print'nbNoeud: %d'%nbNoeud

for i in range(1,nbNoeud):
    node0.add(sys.argv[i])

    
print'sudo service '+sys.argv[nbNoeud]+' '+sys.argv[nbNoeud+1]

task_self().run('sudo service '+sys.argv[nbNoeud]+' '+sys.argv[nbNoeud+1], nodes=node0)

for output, nodes in task_self().iter_buffers():
    for node in nodes:
        print '%s: %s'%(node, output)
