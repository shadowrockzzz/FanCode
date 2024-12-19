import pytest
from fancode.api_client import APIClient
from fancode.user_validator import UserValidation

@pytest.fixture(scope="module")
def api_client():
    client = APIClient()
    yield client
    client.close()

def test(api_client):
    users = api_client.get_users()
    tasks = api_client.get_todos()
    filteredUsers = []
    for user in users:
        if(UserValidation.is_fancode_city(user)):
            filteredUsers.append(user)
    errors = []
    for user in filteredUsers:
        filteredTasks = list(UserValidation.get_user_tasks(user,tasks))
        completedPercentage = UserValidation.get_cpompleted_task_percentage(filteredTasks)
        if (completedPercentage<=50):
            errors.append(f'User with Id {user['id']} has only {completedPercentage: .2f} tasks completed')
    assert len(errors)==0, f'Tests failed for following users:\n'+"\n".join(errors)
