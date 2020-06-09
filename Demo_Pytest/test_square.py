import pytest
import math

@pytest.mark.square
def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5

#Parameterizing of a test is done to run the test against multiple sets of inputs. 
@pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,33),(4,44)])
def test_multiplication_11(num, output):
   assert 11*num == output

#Skipping a test means that the test will not be executed.
@pytest.mark.skip
@pytest.mark.square
def testsquare():
   num = 7
   assert 7*7 == 40

def test_sqrt_failure():
   num = 25
   assert math.sqrt(num) == 6

@pytest.mark.others
def test_equality():
   assert 10 == 10