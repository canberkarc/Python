import datetime

class VehicleRent:
    def __init__(self,stock):
        #stock represents cars' number
        self.stock = stock
        self.now = 0 #it's about determining bill
    
    def displaystock(self): 
        print("{} vehicle available to rent\n".format(self.stock))    
        return self.stock
        
    def rentHourly(self,n):
        if n <= 0:
            print("Number must be positive \n")
            return None
            
        elif n >= self.stock:
            print("Unfortunately {} vehicle available to rent\n".format(self.stock))
    
        else:
            self.now = datetime.datetime.now()
            print("Rented {} vehicle for hourly at {} hours\n".format(n,self.now.hour))
            self.stock -= n
            return self.now
            
    def rentDaily(self,n):
        if n <= 0:
            print("Number must be positive \n")
            return None
            
        elif n >= self.stock:
            print("Unfortunately {} vehicle available to rent\n".format(self.stock))
    
        else:
            self.now = datetime.datetime.now()
            print("Rented {} vehicle for hourly at {} hours\n".format(n,self.now.hour))
            self.stock -= n
            return self.now
        
    #returning a bill    
    def returnVehicle(self,request,brand): 
        car_h_price = 10 #cars' price per hour
        car_d_price = car_h_price*8/10*24 #cars' price per rentDaily
        bike_h_price = 5 #cars' price per hour
        bike_d_price = bike_h_price*7/10*24 #cars' price per rentDaily
        
        rentalTime,rentalBasis,numOfVehicle = request
        bill = 0
        
        if brand == "car":
            if rentalTime and rentalBasis and numOfVehicle:
                self.stock += numOfVehicle
                now = datetime.datetime.now()
                rentalPeriod = rentalTime - now #the time of renting of car
                
                if rentalBasis == 1: #hourly price
                    bill = rentalPeriod.seconds/(3600*car_h_price*numOfVehicle)
                    
                elif rentalBasis == 2: #daily price
                    bill = rentalPeriod.seconds/((3600/24)*car_d_price*numOfVehicle)
            
                if(2 <= numOfVehicle):
                    print("You have extra %20 discount")
                    bill *= 0.8
                    
                print("Thanks for choosing us")
                print("Price : ${}\n".format(round(bill,2)))
                return bill
                
        elif brand == "bike":
            if rentalTime and rentalBasis and numOfVehicle:
                self.stock += numOfVehicle
                now = datetime.datetime.now()
                rentalPeriod = rentalTime - now #the time of renting of bike
                
                if rentalBasis == 1: #hourly price
                    bill = rentalPeriod.seconds/(3600*bike_h_price*numOfVehicle)
                    
                elif rentalBasis == 2: #daily price
                    bill = rentalPeriod.seconds/((3600/24)*bike_d_price*numOfVehicle)
            
                if(4 <= numOfVehicle):
                    print("You have extra %20 discount")
                    bill *= 0.8
                    
                print("Thanks for choosing us")
                print("Price : ${}\n".format(round(bill,2)))
                return bill
                
        else:
            return None
            
class CarRent(VehicleRent):
    
    discount_rate = 15
    
    def __init__(self,stock):
        super().__init__(stock)
        
    def discount(self):
        bill = b - (b*discount_rate)/100
        return bill
        
class BikeRent(VehicleRent):
    def __init(self,stock):
        super().__init__(stock)
    
class Customer:
    def __init__(self):
        self.bikes = 0
        self.rentalBasis_b = 0 #the parameter about renting is hourly or daily
        self.rentalTime_b = 0 #the parameter about when bike is rented
         
        self.cars = 0 
        self.rentalBasis_c = 0 #the parameter about renting is hourly or daily
        self.rentalTime_c = 0 #the parameter about when car is rented
    
    #Function about request bike or car from customer
    def requestVehicle(self,brand):
        if brand == "bike":
            bikes = input("How many bike would you like to rent?\n")
            try:
                bikes = int(bikes)
            except:
                print("Entered value must be a number\n")
                return -1
            
            if bikes < 1:
                print("Number of bikes most be greater than zero\n")
                return -1
            else:
                self.bikes = bikes
                return self.bikes
                
        elif brand == "car":
            cars = input("How many cars you like to rent?\n")
            try:
                cars = int(cars)
            except:
                print("Entered value must be a number\n")
                return -1
            
            if cars < 1:
                print("Number of cars most be greater than zero\n")
                return -1
            else:
                self.cars = cars
                return self.cars
                
        else:
            print("Request vehicle error\n")
            
    #function to return bikes' or cars' informations
    def returnVehicle(self,brand):
        if brand == "bike":
            if self.rentalTime_b and self.rentalBasis_b and self.bikes:
                return self.rentalTime_b,self.rentalBasis_b,self.bikes
            else:
                return 0,0,100
                
        elif brand == "car":
            if self.rentalTime_c and self.rentalBasis_c and self.cars:
                return self.rentalTime_c,self.rentalBasis_c,self.cars
            else:
                return 0,0,0
        else:
            print("Return vehicle error\n")
            
            