import pytest
from click.testing import CliRunner
from app.cli.user_commands import access_resource, update_user_info

@pytest.fixture
def runner():
    return CliRunner()

def test_access_control(runner):
    result = runner.invoke(access_resource, ['unauthorized_user', 'restricted_resource'])
    assert 'Access denied' in result.output

def test_role_upgrade_not_allowed(runner):
    result = runner.invoke(update_user_info, ['unauthorized_user_id', 'admin'])
    assert 'Not authorized to change roles' in result.output

