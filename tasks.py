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



@task
def hi(ctx, name):
  """
  name='Nam'
  invoke build -n $name
  invoke build -n$name

  invoke build --name $name
  invoke build --name=$name

  #no-default-value param can become positional param
  invoke build $name
  """
  displayName = '%s' % name
  print("Hi %s!" % displayName )
