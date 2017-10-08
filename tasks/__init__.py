from invoke import Collection

#the child node
from tasks.c1 import *
from tasks.c2 import *
from tasks.c3 import *
from tasks.c4 import *

c1 = Collection(buildA, buildB)
c2 = Collection(hiA, hiB, hiC)
c3 = Collection(sysTime)
c4 = Collection(task00, task01a, task01b, task02)


#add child to root
ns = namespace = Collection() #the root node
ns.add_collection(c1, name='c1')
ns.add_collection(c2, name='c2')
ns.add_collection(c3, name='c3')
ns.add_collection(c4, name='c4')
