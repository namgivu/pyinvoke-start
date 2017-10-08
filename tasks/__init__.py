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

#TODO how to add c1.c3 to root at module level? We can do it by defining collection n1 va n3 manually at this commit https://github.com/namgivu/pyinvoke-start/commit/b3a56997b7013a4affd56794fc702863945902bf
