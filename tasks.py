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
  name='NN'

  invoke hi -n $name
  invoke hi -n$name

  invoke hi --name $name
  invoke hi --name=$name

  invoke hi $name #no-default-value param can become positional param
  invoke hi -n    #no-default-value param -> this will fail
  """
  print("Hi %s!" % name )
