from ClusterShell.NodeSet import NodeSet, RangeSet
from ClusterShell.Task import task_self
# Constructeurs

node0 = NodeSet()
node0.add('raspberrypi')
node0.add('localhost')

task_self().run('echo Hello World', nodes=node0)

for output, nodes in task_self().iter_buffers():
    for node in nodes:
        print '%s: %s'%(node, output)

task_self().run('sudo service --status-all', nodes=node0)

for output, nodes in task_self().iter_buffers():
    for node in nodes:
        print '%s: %s'%(node, output)
