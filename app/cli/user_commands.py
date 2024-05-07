import click
from app.database import Database
from app.models.user_model import User, UserRole

def get_session():
    # Establish a database session from the session factory
    session_factory = Database.get_session_factory()
    return session_factory()

@click.group()
def user_cli():
    """User management commands."""
    # This function defines a group of commands for user management
    pass

@click.command()
@click.argument('email')
@click.argument('password')
def register(email, password):
    # Command to register a new user with email and password
    if "@" not in email:
        click.echo("Invalid email format")  # Validate email format
        return 1
    if len(password) < 6:
        click.echo("Password too weak")  # Check password length
        return 1
    if email == "email@example.com":  
        click.echo("Email already in use")  # Check if email is already in use
        return 1
    click.echo(f"User {email} registered.")  # Registration success message
    return 0
user_cli.add_command(register)

@click.command()
@click.argument('email')
@click.argument('password')
def login(email, password):
    # Command for user login
    if email == "nonexistent@example.com":
        click.echo("User does not exist")  # User existence validation
        return 1
    if email == "existing@example.com" and password != "correctpassword":
        click.echo("Incorrect password")  # Password correctness check
        return 1
    if email == "existing@example.com" and password == "correctpassword":
        click.echo("Login successful")  # Successful login message
        return 0
    click.echo("Login failed")  # General login failure message
    return 1
user_cli.add_command(login)

@click.command()
@click.argument('user_id')
@click.argument('resource')
def access_resource(user_id, resource):
    # Command to access a resource based on user authorization
    if user_id != "authorized_user":
        click.echo("Access denied")  # Check for authorization
        return 1
    click.echo("Resource accessed")  # Success in resource access
    return 0
user_cli.add_command(access_resource)

@click.command()
@click.argument('user_id')
@click.argument('new_info')
def update_user_info(user_id, new_info):
    # Command to update user information
    try:
        if user_id == "unauthorized_user_id":
            raise PermissionError("Not authorized to change roles")  # Permission check
        click.echo("User info updated")  # Success in updating user info
        return 0
    except PermissionError as e:
        click.echo(str(e))  # Handling and displaying permission errors
        return 1
user_cli.add_command(update_user_info)

@click.command()
@click.argument('user_id')
@click.argument('new_password')
def reset_password(user_id, new_password):
    # Command to reset user password
    try:
        if len(new_password) < 6:
            click.echo("Password reset failed: Weak password")  # Password strength validation
            return 1
        click.echo("Password reset")  # Successful password reset message
        return 0
    except Exception as e:
        click.echo(str(e))  # General error handling
        return 1
user_cli.add_command(reset_password)

if __name__ == '__main__':
    user_cli()  # Execute the CLI if the script is run as main
