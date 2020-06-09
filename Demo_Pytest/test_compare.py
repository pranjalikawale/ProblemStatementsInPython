import pytest

#xfailed test will not be considered as part failed or passed tests. 
@pytest.mark.xfail
#Markers are used to set various features/attributes to test functions.
@pytest.mark.great
def test_greater():
   num = 100
   assert num > 100

@pytest.mark.great
def test_greater_equal():
   num = 100
   assert num >= 100

@pytest.mark.others
def test_less():
   num = 100
   assert num < 200