from ClusterShell.NodeSet import NodeSet, RangeSet
from ClusterShell.Task import task_self
import sys
import dep
import os
#alpha
class service:
    def stop(self, args):
        nodes = NodeSet()
        
        nbNoeud = len(args)-3
        # print'nbNoeud: %d'%nbNoeud
        for i in range(1,nbNoeud):
            node0.add(args[i])

       
        print 'sudo service '+args[nbNoeud+1]+' stop'
        task_self().run('sudo service '+args[nbNoeud+1]+' stop', nodes=nodes)

    def start(self, args, ctrl):
        dependanceManager= dep.dep()
        nodes = NodeSet()
        depNode = NodeSet()
        
        nbNoeud = len(args)-3
        #print'nbNoeud: %d'%nbNoeud
        for i in range(1,nbNoeud):
            node0.add(args[i])

        
        dependance=1
        if os.path.isfile("cfg/"+args[nbNoeud+1]):
            #verification de la dependance
            dependanceManager.toInstall("cfg/"+args[nbNoeud+1])
            dependanceManager.toStart("cfg/"+args[nbNoeud+1])
            
            #recuperation des dependances
            startNode = dependanceManager.getNodeStarted()
            startServices = dependanceManager.getStarted()
            installNode = dependanceManager.getNodeIs_install()
            installService = dependanceManager.getIs_install()

            #pour chaque noeud dependant
            
            for node in installNode:
                depNode.add(node)
                for service in installService:
                    task_self().run('sudo service '+service+' status', nodes=depNode)
                    ret=self.status([node,service,'status'],2)
                    depNode = NodeSet()
                    if ret ==0:
                        print'Service : '+service+' sur : '+node+ ' status : non-installe'
                        dependance = 0
                    elif ret ==1:
                        print'Service : '+service+' sur : '+node+ ' status : installe'
                
            #pour chaque noeud dependant
            for node in startNode:
                depNode.add(node)
                for service in startServices:
                    task_self().run('sudo service '+service+' status', nodes=depNode)
                    ret=self.status([node,service,'status'],1)
                    depNode = NodeSet()
                    if ret ==0:
                        print'Service : '+service+' sur : '+node+ ' status : non-demarre'
                        dependance = 0
                    elif ret ==1:
                        print'Service : '+service+' sur : '+node+ ' status : demarre'
        print dependance
                    
        if dependance == 1:
            print'dependance OK'
            print 'sudo service '+args[nbNoeud+1]+' start'
            task_self().run('sudo service '+args[nbNoeud+1]+' start', nodes=nodes)
        else:
            print'dependance KO'

    def status(self, args,afficher):
        node0 = NodeSet()
        nbNoeud = len(args)-3
        
        #print'nbNoeud: %d'%nbNoeud
    
        for i in range(1,nbNoeud):
            node0.add(args[i])

        print 'sudo service '+args[nbNoeud+1]+' status'
        task_self().run('sudo service '+args[nbNoeud+1]+' status', nodes=node0)
      
        return self.recevoir(afficher)

    def recevoir(self,ctrl):
        #ctrl==1=start, ctrl==2=install, ctrl!=0=afficher
        if ctrl != 0:
            
            for output, nodes in task_self().iter_buffers():
               for node in nodes:
                   print '%s: %s'%(node, output)
                   # a tester
                   string='%s'%output
                   if ctrl == 2:
                        if string.split('Loaded: ')[1].split(' ')[0]=='loaded':
                            print '%s install status : 1'%node
                            return 1
                        elif string.split('Loaded: ')[1].split(' ')[0]=='not-found':
                            print '%s install status : 0'%node
                            return 0
                        else :
                            print '%s install status : inconnu'%node
                            return -1
            
                   if ctrl == 1:
                       
                        if string.split('Active: ')[1].split(' ')[0]=='active':
                            print '%s start status : 1'%node
                            return 1
                        elif string.split('Active: ')[1].split(' ')[0]=='inactive':
                            print '%s start status : 0'%node
                            return 0
                        else :
                            print '%s start status : inconnu'%node
                            return -1
                
           # "Active:" "active" "inactive"    
            

if __name__ == "__main__":
    services = service()
    if sys.argv[len(sys.argv)-1]=='start':
        services.start(sys.argv,0)
    elif sys.argv[len(sys.argv)-1]=='status':
        services.status(sys.argv,0)
    elif sys.argv[len(sys.argv)-1]=='stop':
        services.stop(sys.argv)

    #sudo python service.py localhost dhcpcd status
    
   
