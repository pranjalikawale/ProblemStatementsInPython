
class QuantityMeasurement():

    def __init__(self):
        self.quantity=0
        
    def get_measurement(self,quantity_category,quantity):
        if quantity>0:
            self.quantity=quantity_category.value*quantity
        return max([self.quantity,0.0])
        

