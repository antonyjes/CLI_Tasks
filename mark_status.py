import click
from utils import load_json, save_json
import datetime


# Mark task as done
@click.command()
@click.argument('id')
def mark_done(id):
    data = load_json("tasks.json")

    for task in data['tasks']:
        if task['id'] == id:
            task['status'] = 'done'
            task['updatedAt'] = datetime.datetime.now().isoformat()
            break

    save_json("tasks.json", data)

    click.echo("Task marked as done successfully!")


# Mark task as in progress
@click.command()
@click.argument('id')
def mark_in_progress(id):
    data = load_json("tasks.json")

    for task in data['tasks']:
        if task['id'] == id:
            task['status'] = 'in-progress'
            task['updatedAt'] = datetime.datetime.now().isoformat()
            break

    save_json("tasks.json", data)

    click.echo("Task marked as in progress successfully!")