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
@task
def hi(ctx, name):
  """
  name='NN'

  invoke hi -n $name
  invoke hi -n$name

  invoke hi --name $name
  invoke hi --name=$name

  invoke hi $name #no-default-value param can become positional param
  invoke hi -n    #no-default-value param -> this will fail
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
  displayName = '%s' % name
  print("Hello %s!" % displayName )
#endregion positional param


@task
def sysTime(ctx):
  ctx.run('date')
