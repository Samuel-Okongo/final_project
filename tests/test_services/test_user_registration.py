import pytest
from click.testing import CliRunner
from app.cli.user_commands import register

# pytest fixture to initialize the Click test runner
@pytest.fixture
def runner():
    # Creates a new instance of CliRunner, which is used to invoke the CLI commands
    return CliRunner()

# Test function to verify registration with missing fields
def test_register_with_missing_fields(runner):
    # Invokes the register command with only the email provided, omitting the password
    result = runner.invoke(register, ['email@example.com'])
    # Checks if the output from the command indicates a missing argument error
    assert "Missing argument" in result.output

# Test function to verify registration with an invalid email format
def test_register_with_invalid_email(runner):
    # Invokes the register command with an incorrectly formatted email address
    result = runner.invoke(register, ['not-an-email', 'password123'])
    # Checks if the output from the command contains 'Invalid email format'
    assert 'Invalid email format' in result.output

# Test function to verify registration with an email that is already in use
def test_register_duplicate_email(runner):
    # Invokes the register command with an email that has been used previously
    result = runner.invoke(register, ['email@example.com', 'StrongPassword123'])
    # Checks if the output from the command states that the email is already in use
    assert 'Email already in use' in result.output

# Test function to verify registration with a weak password
def test_register_weak_password(runner):
    # Invokes the register command with a weak password
    result = runner.invoke(register, ['valid@example.com', '123'])
    # Checks if the output from the command contains 'Password too weak'
    assert 'Password too weak' in result.output

