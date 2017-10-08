from invoke import Collection

#the child node
import tasks.c1
import tasks.c2
import tasks.c4

#add child to root
ns = namespace = Collection() #the root node
ns.add_collection(c1, name='c1')
ns.add_collection(c2, name='c2')
ns.add_collection(c4, name='c4')
