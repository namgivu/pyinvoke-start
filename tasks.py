from invoke import task


@task
def build(ctx):
  print("Building!")


@task
def build(ctx, clean=False):
  """
  invoke build -c
  invoke build --clean
  """
  if clean:
    print("Cleaning!")
  print("Building!")


#region positional param
pass

@task
def hi(ctx, name):
  """
  name='NN'

  invoke hi -n $name
  invoke hi -n$name

  invoke hi --name $name
  invoke hi --name=$name

  invoke hi $name #no-default-value param can become positional param
  invoke hi -n    #no-default-value param -> this will fail; see how to make it work at `invoke halo -n`
  """
  print("Hi %s!" % name )


@task
def hello(ctx, name='SomeDefaultName'):
  """
  #similar usage as `invoke hi`

  #but this works even no argument given (default one is used i.e. 'SomeDefaultName')
  invoke hello

  #though with default-value, this i.e positional-param WON'T work
  name='NN'
  invoke hello $name
  """
  print("Hello %s!" % name )


@task(optional=['name'])
def halo(ctx, name):
  """
  #similar usage as `invoke hi`; but make `invoke hi -n` work
  """
  print("Hello %s!" % name )

pass
#endregion positional param


@task
def sysTime(ctx):
  ctx.run('date')


#region pre-task
pass

@task
def task00(ctx):
  print('task00')


@task(task00)
def task01b(ctx):
  print('task01b')


@task(pre=[task00])
def task01a(ctx):
  print('task01a')

pass
#endregion pre-task
