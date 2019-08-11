"""The calculator interface"""

import click
from project.lib import operations

print(dir(operations))


@click.group()
def cli():
    """A simple calculator."""
    pass


@cli.command()
@click.argument("a")
@click.argument("b")
def add(a, b):
    """Add two numbers."""
    print(operations.add(float(a), float(b)))


@cli.command()
@click.argument("a")
@click.argument("b")
def sub(a, b):
    """Subtract two numbers."""
    print(operations.sub(float(a), float(b)))


@cli.command()
@click.argument("a")
@click.argument("b")
def mult(a, b):
    """Multiply two numbers."""
    print(operations.mult(float(a), float(b)))


@cli.command()
@click.argument("a")
@click.argument("b")
def div(a, b):
    """Divide two numbers."""
    print(operations.div(float(a), float(b)))


if __name__ == "__main__":
    cli()
