from tires.tires import Tires
import array as arr

class Carrigan(Tires):

    
    def __init__(self, how_much_each_tire_is_worn):
        tire1 = None
        tire2 = None
        tire3 = None
        tire4 = None

        self.how_much_each_tire_is_worn = how_much_each_tire_is_worn 
        
        
    def needs_service(self):    
        for i in (0,5):
            if self.how_much_each_tire_is_worn[i] < 0:
                return "wrong input"
            if self.how_much_each_tire_is_worn[i] >= 0.9:
                return True
            else:
                return False    