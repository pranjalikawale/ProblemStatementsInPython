import pytest
from quantity_measurement import QuantityMeasurement

@pytest.fixture
def quantity_measurement_object():
    quantity_object=QuantityMeasurement()
    return quantity_object
     