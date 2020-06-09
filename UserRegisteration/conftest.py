import pytest
from user_registeration import UserRegisteration

@pytest.fixture
def user_registeration_object():
   user_registeration_object=UserRegisteration()
   return user_registeration_object
