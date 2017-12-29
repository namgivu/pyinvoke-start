We use Python 3 and run under virtualenv
```
virtualenv -p python3 ./venv3
source ./venv3/bin/activate
```

Code starts at 
`/home/namgivu/NN/code/_NN_/pyinvoke-start/tasks/__init__.py`

Print all tasks
```
invoke --list
```

references
The practice/get-started guide is referenced here 
http://docs.pyinvoke.org/en/latest/getting_started.html

Put task into collection/namespace
http://docs.pyinvoke.org/en/latest/concepts/namespaces.html#nesting-collections
set default task for namespace
http://docs.pyinvoke.org/en/latest/concepts/namespaces.html#default-tasks
