from enum import Enum
import math

class Quantity(Enum):
    FEETTOINCH=12
    INCHTOFEET=0.084
    FEETTOYARD=0.334
    YARDTOFEET=3
    INCHTOYARD=0.028
    YARDTOINCH=36
    CENTIMETERTOINCH=0.40
    INCHTOCENTIMETER=2.54
    LITERTOMILILITER=1000
    MILILITERTOLITER=0.001
    GALLONTOLITER=3.78
    LITERTOGALLON=0.265
    KILOGRAMTOGRAM=1000
    GRAMTOKILOGRAM=0.001
    TONTOKILOGRAM=1000
    KILOGRAMTOTON=0.00113

    def __init__(self,measurement):
        self.measurement=measurement
    
    @property
    def getMeasurement(self,quantity):
        if quantity>0:
            quantity*=self.measurement
        return max([quantity,0.0])

