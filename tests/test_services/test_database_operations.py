import pytest
from click.testing import CliRunner
from app.cli.user_commands import user_cli

@pytest.fixture
def runner():
    return CliRunner()

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    invalid_database_url = "postgresql+asyncpg://invalid:invalid@localhost/invalid_db"
    try:
        from app.database import Database
        Database.initialize(invalid_database_url)
    except Exception:
        pass  # We expect this to fail, hence no action is taken

def test_database_connection_failure(runner):
    result = runner.invoke(user_cli, ['reset_password', 'user_id', 'new_password'])
    assert result.exit_code != 0, "Expected non-zero exit code when database connection fails"

def test_transaction_rollback_on_error(runner):
    result = runner.invoke(user_cli, ['update_user_info', 'user_id', 'new_info'])
    assert result.exit_code != 0, "Expected non-zero exit code when transaction fails"
