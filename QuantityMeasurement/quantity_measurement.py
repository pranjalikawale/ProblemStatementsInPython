from quantity import Quantity,Unit

class QuantityMeasurement():

    def __init__(self):
        self.quantity=0

    def get_measurement(self,quantity_category,quantity):
        if quantity>0:
            self.quantity=quantity_category.value*quantity
        return max([self.quantity,0.0])

    def check_equality(self,quantity_type1,value_1,quantity_type2,value_2):
        if self.check_type(quantity_type1,quantity_type2):
            value_1=self.convert_unit(quantity_type1,value_1,quantity_type2)
        return self.check_for_value_equality(value_1,value_2)
    
    def check_type(self,quantity_type1,quantity_type2):
        if quantity_type1!=quantity_type2:
            return True
        return False
    
    def convert_unit(self,quantity_type1,value_1,quantity_type2): 
        quantity_type3=quantity_type1.name+"TO"+quantity_type2.name
        value_1=self.get_measurement(Quantity(quantity_type3),value_1)
        return value_1
    
    def check_for_value_equality(self,value_1,value_2):
        if value_1==value_2:
            return True
        return False

    #check for equality
    def equals(self,quantity_measurement_object):
        if quantity_measurement_object !=None and isinstance(quantity_measurement_object,QuantityMeasurement) and quantity_measurement_object.quantity==self.quantity:
            return True
        return False


