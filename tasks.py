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

