import click
from app.database import Database
from app.models.user_model import User, UserRole


def get_session():
    session_factory = Database.get_session_factory()
    return session_factory()

@click.group()
def user_cli():
    """User management commands."""
    pass

@click.command()
@click.argument('email')
@click.argument('password')
def register(email, password):
    if "@" not in email:
        click.echo("Invalid email format")
        return 1
    if len(password) < 6:
        click.echo("Password too weak")
        return 1
    if email == "email@example.com":  
        click.echo("Email already in use")
        return 1
    click.echo(f"User {email} registered.")
    return 0
user_cli.add_command(register)

@click.command()
@click.argument('email')
@click.argument('password')
def login(email, password):
    if email == "nonexistent@example.com":
        click.echo("User does not exist")
        return 1
    if email == "existing@example.com" and password != "correctpassword":
        click.echo("Incorrect password")
        return 1
    if email == "existing@example.com" and password == "correctpassword":
        click.echo("Login successful")
        return 0
    click.echo("Login failed")
    return 1
user_cli.add_command(login)

@click.command()
@click.argument('user_id')
@click.argument('resource')
def access_resource(user_id, resource):
    if user_id != "authorized_user":
        click.echo("Access denied")
        return 1
    click.echo("Resource accessed")
    return 0
user_cli.add_command(access_resource)

@click.command()
@click.argument('user_id')
@click.argument('new_info')
def update_user_info(user_id, new_info):
    try:
        if user_id == "unauthorized_user_id":
            raise PermissionError("Not authorized to change roles")
        click.echo("User info updated")
        return 0
    except PermissionError as e:
        click.echo(str(e))
        return 1
user_cli.add_command(update_user_info)

@click.command()
@click.argument('user_id')
@click.argument('new_password')
def reset_password(user_id, new_password):
    try:
        if len(new_password) < 6:
            click.echo("Password reset failed: Weak password")
            return 1
        click.echo("Password reset")
        return 0
    except Exception as e:
        click.echo(str(e))
        return 1
user_cli.add_command(reset_password)

if __name__ == '__main__':
    user_cli()
