# tests/test_services/test_user_registration.py

import pytest
from click.testing import CliRunner
from app.cli.user_commands import register

@pytest.fixture
def runner():
    return CliRunner()

def test_register_with_missing_fields(runner):
    result = runner.invoke(register, ['email@example.com'])
    assert "Missing argument" in result.output

def test_register_with_invalid_email(runner):
    result = runner.invoke(register, ['not-an-email', 'password123'])
    assert 'Invalid email format' in result.output

def test_register_duplicate_email(runner):
    result = runner.invoke(register, ['email@example.com', 'StrongPassword123'])
    assert 'Email already in use' in result.output

def test_register_weak_password(runner):
    result = runner.invoke(register, ['valid@example.com', '123'])
    assert 'Password too weak' in result.output
