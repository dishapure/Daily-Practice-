class Car: 
    def __init__(self, name, brand):
        self.name  = name
        self.brand = brand 
        
    def info(self):
        return f"{self.brand} Car"
    
class Bike(Car):
    def __init__(self, name, brand, type):
        super().__init__(name, brand) 
        self.type = type
        
    def info(self):
        return f"{self.type} Bike"
    
vehicles = [Car ("SUV", "Toyota"), Bike("Commuter", "Honda", "Mountain")] 
for vehicle in vehicles:
    print(vehicle.info())