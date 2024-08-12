import click
from utils import load_json, save_json
import uuid
import datetime


# Create a new task
@click.command()
@click.argument('name')
def add_task(name):
    new_task = {
        "id": str(uuid.uuid4()),
        "name": name,
        "status": "todo",
        "createdAt": datetime.datetime.now().isoformat(),
        "updatedAt": datetime.datetime.now().isoformat()
    }

    data = load_json("tasks.json")

    data['tasks'].append(new_task)

    save_json("tasks.json", data)

    click.echo("Task added successfully!")


# Read the list of tasks
@click.command()
def list_tasks():
    data = load_json("tasks.json")

    click.echo("ID | NAME | STATUS")
    for task in data['tasks']:
        click.echo(f"{task['id']} | {task['name']} | {task['status']}")