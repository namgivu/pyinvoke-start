from invoke import task

"""
call os commands
"""


@task
def sysTime(ctx):
  """
  call os commands e.g. date, ls, etc.
  """
  ctx.run('date')
