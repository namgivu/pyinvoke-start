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
  invoke buildC --name='Ana Amerson'
  """
  print("Hi{}!".format(' '+name if name else ''))


@task
def buildD(ctx, firstName=None, lastName=None):
  """
  task with params
  invoke c1.buildD
  invoke c1.buildD -f=Ana      -l=Amerson
  invoke c1.buildD -f='Ana bb' -l='Amerson ccc'
  """
  print("Hi{}{}!".format(
    ' '+firstName if firstName else '',
    ' '+lastName if lastName else '',
  ))


@task
def buildD2(ctx, firstName, lastName):
  """
  task with params
  invoke c1.buildD2
  """
  print("Hi{}{}!".format(
    ' '+firstName if firstName else '',
    ' '+lastName if lastName else '',
  ))


@task
def generate_report(context, software, version):
  """
  invoke c1.generate_report -s='/tmp/YYmmDD-hhMMss.exe' -v='ABB-122333'

  #TODO why this NOT working i.e. --version not working while -v do work
  invoke c1.generate_report -s='/tmp/YYmmDD-hhMMss.exe' --version='ABB-122333'
  """
  print("{},{}!".format(
    software,
    version,
  ))
