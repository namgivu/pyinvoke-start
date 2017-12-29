from invoke import task


"""
task basic
"""


@task
def buildA(ctx):
  """
  hello world task
  invoke c1.buildA
  """
  print("Hello world!")


@task
def buildB(ctx, clean=False):
  """
  task with param basic
  invoke c1.buildB -c
  invoke c1.buildB --clean
  """
  if clean: print("Cleaning!")
  print("Hello world!")


@task
def buildC(ctx, name=None):
  """
  task with params
  invoke buildC --name=Ana
  """
  print("Hello world{}!".format(' '+name if name else ''))

