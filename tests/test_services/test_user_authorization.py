import pytest
from click.testing import CliRunner
from app.cli.user_commands import access_resource, update_user_info

# pytest fixture to initialize the Click test runner
@pytest.fixture
def runner():
    # Creates a new instance of CliRunner, which is used to invoke the CLI commands
    return CliRunner()

# Test function to verify access control to a restricted resource
def test_access_control(runner):
    # Invokes the access_resource command with an unauthorized user trying to access a restricted resource
    result = runner.invoke(access_resource, ['unauthorized_user', 'restricted_resource'])
    # Checks if the output from the command contains 'Access denied'
    assert 'Access denied' in result.output

# Test function to verify that unauthorized users cannot upgrade roles
def test_role_upgrade_not_allowed(runner):
    # Invokes the update_user_info command with an unauthorized user ID attempting to upgrade to an admin role
    result = runner.invoke(update_user_info, ['unauthorized_user_id', 'admin'])
    # Checks if the output from the command contains 'Not authorized to change roles'
    assert 'Not authorized to change roles' in result.output
