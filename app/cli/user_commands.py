import click
import uuid
from sqlalchemy.orm import Session
from app.database import engine  # Ensure you have a way to get your database engine/session
from app.models.user_model import User, UserRole

# Creating a session
def get_session():
    return Session(bind=engine)

@click.group(name='user')
def user_cli():
    """User management commands."""
    pass

@user_cli.command(name='change-role')
@click.argument('user_id', type=uuid.UUID)
@click.argument('new_role', type=click.Choice([role.name for role in UserRole]))
def change_role(user_id, new_role):
    """Change the role of a user."""
    session = get_session()
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        user.role = UserRole[new_role]
        session.commit()
        click.echo(f"Role for user {user.nickname} changed to {new_role}.")
    else:
        click.echo("User not found.")
    session.close()

@user_cli.command(name='lock-account')
@click.argument('user_id', type=uuid.UUID)
def lock_account(user_id):
    """Lock a user's account."""
    session = get_session()
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        user.lock_account()
        session.commit()
        click.echo(f"Account for user {user.nickname} locked.")
    else:
        click.echo("User not found.")
    session.close()

@user_cli.command(name='unlock-account')
@click.argument('user_id', type=uuid.UUID)
def unlock_account(user_id):
    """Unlock a user's account."""
    session = get_session()
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        user.unlock_account()
        session.commit()
        click.echo(f"Account for user {user.nickname} unlocked.")
    else:
        click.echo("User not found.")
    session.close()

@user_cli.command(name='verify-email')
@click.argument('user_id', type=uuid.UUID)
def verify_email(user_id):
    """Verify a user's email."""
    session = get_session()
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        user.verify_email()
        session.commit()
        click.echo(f"Email for user {user.nickname} verified.")
    else:
        click.echo("User not found.")
    session.close()

if __name__ == '__main__':
    user_cli()
