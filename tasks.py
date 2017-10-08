from invoke import task


@task
def buildA(ctx):
  print("Building!")


@task
def buildB(ctx, clean=False):
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
def hiA(ctx, name):
  """
  name='NN'

  invoke hiA -n $name
  invoke hiA -n$name

  invoke hiA --name $name
  invoke hiA --name=$name

  invoke hiA $name #no-default-value param can become positional param
  invoke hiA -n    #no-default-value param -> this will fail; see how to make it work at `invoke halo -n`
  """
  print("Hi %s!" % name )


@task
def hiB(ctx, name='SomeDefaultName'):
  """
  #similar usage as `invoke hiA`

  #but this works even no argument given (default one is used i.e. 'SomeDefaultName')
  invoke hiB

  #though with default-value, this i.e positional-param WON'T work
  name='NN'
  invoke hiB $name
  """
  print("Hi %s!" % name )


@task(optional=['name'])
def hiC(ctx, name):
  """
  #similar usage as `invoke hiA`; but make `invoke hiA -n` work via `optional` ref. http://docs.pyinvoke.org/en/latest/concepts/cli/intro.html#optional-flag-values
  """
  print("Hi %s!" % name )

pass
#endregion positional param


@task
def sysTime(ctx):
  ctx.run('date')


#region pre/post task
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


@task(post=[task00])
def task02(ctx):
  print('task02')

pass
#endregion pre-task
