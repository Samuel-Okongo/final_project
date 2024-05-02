import click
from .database_commands import database_cli
from .user_commands import user_cli

@click.group()
def cli():
    """Admin Console Application for User Management System."""
    pass

cli.add_command(database_cli)
cli.add_command(user_cli)

if __name__ == '__main__':
    cli()
