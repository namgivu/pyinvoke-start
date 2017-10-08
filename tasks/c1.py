from invoke import task


"""
task basic
"""


@task
def buildA(ctx):
  """
  hello world task
  """
  print("Hello world!")


@task
def buildB(ctx, clean=False):
  """
  task with param basic
  invoke buildB -c
  invoke buildB --clean
  """
  if clean:
    print("Cleaning!")
  print("Hello world!")

