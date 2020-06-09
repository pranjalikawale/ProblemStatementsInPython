import pytest

#Fixtures are functions, which will run before each test function to which it is applied.
#Fixtures are used to feed some data to the tests such as database connections, 
#URLs to test and some sort of input data.
@pytest.fixture
def input_value():
   input = 39
   return input