import pytest
from click.testing import CliRunner
from app.cli.user_commands import login

@pytest.fixture
def runner():
    return CliRunner()

def test_correct_login(runner):
    result = runner.invoke(login, ['existing@example.com', 'correctpassword'])
    assert 'Login successful' in result.output

def test_incorrect_password(runner):
    result = runner.invoke(login, ['existing@example.com', 'wrongpassword'])
    assert 'Incorrect password' in result.output

def test_login_nonexistent_user(runner):
    result = runner.invoke(login, ['nonexistent@example.com', 'any_password'])
    assert 'User does not exist' in result.output
