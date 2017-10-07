from invoke import task


@task
def build(ctx):
    print("Building!")


@task
def build(ctx, clean=False):
    if clean:
        print("Cleaning!")
    print("Building!")