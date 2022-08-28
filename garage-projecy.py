# Your parking gargage class should have the following methods:
# - takeTicket
# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parkingSpaces available by 1
# - payForParking
# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True
# - leaveGarage
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)

# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary

class ParkingGarage:
    def __init__(self, tickets = [], parking_spaces = [], current_ticket = {'paid' : False}):
        self.tickets = [x for x in range(1,20)]
        self.parking_spaces = [x for x in range(1,20)]
        self.current_ticket = {}       
    
    def takeTicket(self):
        print("Please take your ticket!")
        print(f"\n{len(self.parking_spaces)} spots remaining")

        self.current_ticket = {'paid' : False}
        self.parking_spaces = self.parking_spaces[:-1]
        self.tickets = self.tickets[:-1]

    def pay(self):
        hours = input("How many hours did you use the parking garage for? ")    
        price = int(hours) * 3
        print(f"The total cost for parking is {price}$.")
        while True:
            payment = input("Would you like to pay? - yes/no ")


            if payment == 'yes':
                self.current_ticket = {'paid': True}
                price = int(hours) * 3
                print("=~" * 15)
                print("-~=        TICKET        =~-")
                print("\n" * 2)
                print(f"The total cost for parking is {price}$.")
                print("\nThank you for paying! You have 15 minutes to leave or perish.")
                print("\n" * 2)
                print("=~" * 15)
                break

            elif payment == 'no':
                self.current_ticket = {'paid': False}
                print("Please pay your ticket to exit. ")     
                continue
                
            else:
                self.current_ticket = {'paid': False}
                print("Please enter a valid payment ")

    def leave(self):
        if self.current_ticket == {'paid': False}:
            print('Please pay your ticket to exit. ')
            self.pay()

        elif self.current_ticket == {'paid': True}:

            for num in range(len(self.parking_spaces), 20):
                self.parking_spaces.append(num)
            for num in range(len(self.tickets), 20):
                self.tickets.append(num)   
            print("Thank you! Have a nice day! ")
        
        


            
my_garage = ParkingGarage()

def run():
    while True:
        response = input("What would you like to do? enter/pay/spots/leave ")
        if response.lower() == 'enter':
            my_garage.takeTicket()
        
        elif response.lower() == 'pay':
            my_garage.pay()
                

        elif response.lower() == 'spots':
            print(f"{len(my_garage.parking_spaces)} spots remaining.")

        elif response.lower() == 'leave':
            my_garage.leave()
            break
        
        else:
            print("Invalid Entry.")

run()