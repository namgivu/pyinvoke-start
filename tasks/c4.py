from invoke import task

"""
region pre/post task
"""


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
