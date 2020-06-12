import pytest
from quantity_measurement import QuantityMeasurement
from quantity import Quantity,Unit

class TestQuantityMeasurement:

    def test_pass_when_given_feet_is_valid_should_return_inch(self,quantity_measurement_object):
        assert quantity_measurement_object.get_measurement(Quantity.FEETTOINCH,1)==12

    def test_pass_when_given_feet_is_zero_should_return_zero_inch(self,quantity_measurement_object):
        assert quantity_measurement_object.get_measurement(Quantity.FEETTOINCH,0)==0.0

    def test_pass_when_given_feet_is_invalid_should_return_zero_inch(self,quantity_measurement_object):
        assert quantity_measurement_object.get_measurement(Quantity.FEETTOINCH,-1)==0.0
 
    def test_pass_when_given_zero_feet_zero_feet_when_equal_should_return_true(self,quantity_measurement_object):
        assert quantity_measurement_object.check_equality(Unit.FEET,0,Unit.FEET,0)==True

    def test_pass_when_given_object_when_null_should_return_false(self,quantity_measurement_object):
        assert quantity_measurement_object.equals(None)==False

    def test_pass_check_for_object_when_equal_should_return_true(self,quantity_measurement_object):
        assert quantity_measurement_object.equals(quantity_measurement_object)==True    

    def test_pass_check_for_object_when_not_equal_should_return_false(self,quantity_measurement_object):
        quantity_measurement_object.get_measurement(Quantity.FEETTOINCH,1)
        assert quantity_measurement_object.equals(TestQuantityMeasurement())==False

    def test_pass_check_for_value_when_equal_should_return_true(self,quantity_measurement_object):
        quantity_measurement_object.get_measurement(Quantity.FEETTOINCH,1)
        quantity_object=QuantityMeasurement()
        quantity_object.get_measurement(Quantity.FEETTOINCH,1)
        assert quantity_measurement_object.equals(quantity_object)==True

    def test_pass_check_for_value_when_not_equal_should_return_false(self,quantity_measurement_object):
        quantity_measurement_object.get_measurement(Quantity.FEETTOINCH,1)
        quantity_object=QuantityMeasurement()
        quantity_object.get_measurement(Quantity.FEETTOINCH,2)
        assert quantity_measurement_object.equals(quantity_object)==False
            

    

    

    
        