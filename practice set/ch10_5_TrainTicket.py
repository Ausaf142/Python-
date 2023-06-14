class Train:

    def __init__(self,name,seat,fare):
        self.name=name
        self.seat=seat
        self.fare=fare
        
    def getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train is {self.seat}")
    def getFare(self):
        print(f"The fare of the ticket is Rs {self.fare}")
    def bookTicket(self):
        if(self.seat>0):
           print(f"Your ticket has been booked Seat no is {self.seat}")
           self.seat=self.seat-1
        else:
            print("Seats Not available,Plz go for Tatkal")

intercity=Train("Bihar Sampark:22417",2,90)    
# intercity.getStatus()
# intercity.getFare()
intercity.bookTicket()
intercity.bookTicket()
intercity.getStatus()
intercity.bookTicket()

