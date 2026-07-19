from testing import UserManager
import pytest

@pytest.fixture
def user_manager():
    return UserManager()

def test_add_user(user_manager):
    assert user_manager.add_user("john12", "john@gmail.com") == True
    assert user_manager.get_user("john12") == "john@gmail.com"
