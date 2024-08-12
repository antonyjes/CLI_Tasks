import click
from utils import load_json


# List tasks by status in-progress
@click.command()
def list_in_progress():
    data = load_json("tasks.json")

    click.echo("ID | NAME | STATUS")
    for task in data['tasks']:
        if task['status'] == 'in-progress':
            click.echo(f"{task['id']} | {task['name']} | {task['status']}")


# List tasks by status todo
@click.command()
def list_todo():
    data = load_json("tasks.json")

    click.echo("ID | NAME | STATUS")
    for task in data['tasks']:
        if task['status'] == 'todo':
            click.echo(f"{task['id']} | {task['name']} | {task['status']}")


# List tasks by status done
@click.command()
def list_done():
    data = load_json("tasks.json")

    click.echo("ID | NAME | STATUS")
    for task in data['tasks']:
        if task['status'] == 'done':
            click.echo(f"{task['id']} | {task['name']} | {task['status']}")