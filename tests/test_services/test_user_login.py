import pytest
from click.testing import CliRunner
from app.cli.user_commands import login

# pytest fixture to initialize the Click test runner
@pytest.fixture
def runner():
    # Creates a new instance of CliRunner, which is used to invoke the CLI commands
    return CliRunner()

# Test function to check the login functionality with correct credentials
def test_correct_login(runner):
    # Invokes the login command with a known correct email and password
    result = runner.invoke(login, ['existing@example.com', 'correctpassword'])
    # Checks if the output from the command contains 'Login successful'
    assert 'Login successful' in result.output

# Test function to check the login functionality with an incorrect password
def test_incorrect_password(runner):
    # Invokes the login command with a correct email but incorrect password
    result = runner.invoke(login, ['existing@example.com', 'wrongpassword'])
    # Checks if the output from the command contains 'Incorrect password'
    assert 'Incorrect password' in result.output

# Test function to check the login functionality for a nonexistent user
def test_login_nonexistent_user(runner):
    # Invokes the login command with a non-existing email
    result = runner.invoke(login, ['nonexistent@example.com', 'any_password'])
    # Checks if the output from the command contains 'User does not exist'
    assert 'User does not exist' in result.output
