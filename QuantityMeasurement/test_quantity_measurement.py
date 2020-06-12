import pytest
from quantity_measurement import QuantityMeasurement
from quantity import Quantity

class TestQuantityMeasurement:

    def test_pass_when_given_feet_is_valid_should_return_inch(self,quantity_measurement_object):
        assert quantity_measurement_object.get_measurement(Quantity.FEETTOINCH,1)==12

    def test_pass_when_given_feet_is_zero_should_return_zero_inch(self,quantity_measurement_object):
        assert quantity_measurement_object.get_measurement(Quantity.FEETTOINCH,0)==0.0

    def test_pass_when_given_feet_is_invalid_should_return_zero_inch(self,quantity_measurement_object):
        assert quantity_measurement_object.get_measurement(Quantity.FEETTOINCH,-1)==0.0

    

    

    
        