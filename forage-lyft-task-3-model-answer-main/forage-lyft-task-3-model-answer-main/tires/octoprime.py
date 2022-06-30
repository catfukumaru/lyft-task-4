from tires import tires
import array as arr

class Octoprime(Tires):
    def __init__(self):
        tire1 = None
        tire2 = None
        tire3 = None
        tire4 = None
        self.how_much_each_tire_is_worn = arr.array('d', [tire1, tire2, tire3, tire4])
    
    def needs_service(self):
        result=0    
        for i in (0,5):
            result += self.how_much_each_tire_is_worn[i]
            if result >= 3:
                return True
            else:
                return False    

        