import click
import json
import uuid
import datetime

@click.group()
def cli():
    pass


@cli.command()
@click.argument('name')
def add_task(name):
    new_task = {
        "id": str(uuid.uuid4()),
        "name": name,
        "status": "todo",
        "createdAt": datetime.datetime.now().isoformat(),
        "updatedAt": datetime.datetime.now().isoformat()
    }

    with open('tasks.json', 'r') as f:
        data = json.load(f)
    
    data['tasks'].append(new_task)

    with open('tasks.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    click.echo("Task added successfully!")


@cli.command()
def list_tasks():
    with open('tasks.json', 'r') as f:
        data = json.load(f)
    
    click.echo("ID | Name | Status")
    for task in data['tasks']:
        click.echo(f"{task['id']} | {task['name']} | {task['status']}")


@cli.command()
@click.argument('id')
def delete_task(id):
    with open('tasks.json', 'r') as f:
        data = json.load(f)
    
    for task in data['tasks']:
        if task['id'] == id:
            data['tasks'].remove(task)
            break
    
    with open('tasks.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    click.echo("Task deleted successfully!")


@cli.command()
@click.argument('id')
@click.argument('new_name')
def update_task(id, new_name):
    with open('tasks.json', 'r') as f:
        data = json.load(f)
    
    for task in data['tasks']:
        if task['id'] == id:
            task['name'] = new_name
            break
    
    with open('tasks.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    click.echo("Task updated successfully!")


@cli.command()
@click.argument('id')
def mark_in_progress(id):
    with open('tasks.json', 'r') as f:
        data = json.load(f)
    
    for task in data['tasks']:
        if task['id'] == id:
            task['status'] = "in-progress"
            break
    
    with open('tasks.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    click.echo("Task marked as in-progress successfully!")


@cli.command()
@click.argument('id')
def mark_done(id):
    with open('tasks.json', 'r') as f:
        data = json.load(f)
    
    for task in data['tasks']:
        if task['id'] == id:
            task['status'] = "done"
            break
    
    with open('tasks.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    click.echo("Task marked as done successfully!")


@cli.command()
def list_in_progress():
    with open('tasks.json', 'r') as f:
        data = json.load(f)
    
    click.echo("ID | Name | Status")
    for task in data['tasks']:
        if task['status'] == 'in-progress':
            click.echo(f"{task['id']} | {task['name']} | {task['status']}")


@cli.command()
def list_todo():
    with open('tasks.json', 'r') as f:
        data = json.load(f)
    
    click.echo("ID | Name | Status")
    for task in data['tasks']:
        if task['status'] == 'todo':
            click.echo(f"{task['id']} | {task['name']} | {task['status']}")
            

@cli.command()
def list_done():
    with open('tasks.json', 'r') as f:
        data = json.load(f)
    
    click.echo("ID | Name | Status")
    for task in data['tasks']:
        if task['status'] == 'done':
            click.echo(f"{task['id']} | {task['name']} | {task['status']}")


if __name__ == '__main__':
    cli()