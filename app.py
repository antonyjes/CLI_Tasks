import click
from crud import add_task

@click.group()
def cli():
    pass


cli.add_command(add_task)


if __name__ == '__main__':
    cli()