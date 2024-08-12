import click
from crud import add_task, list_tasks, update_task, delete_task
from list_by_status import list_in_progress, list_todo, list_done

@click.group()
def cli():
    pass

# Main CRUD commands
cli.add_command(add_task)
cli.add_command(list_tasks)
cli.add_command(update_task)
cli.add_command(delete_task)

# Commands to list tasks by status
cli.add_command(list_in_progress)
cli.add_command(list_todo)
cli.add_command(list_done)


if __name__ == '__main__':
    cli()