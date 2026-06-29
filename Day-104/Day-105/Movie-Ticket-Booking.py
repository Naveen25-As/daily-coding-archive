# Movie Ticket Booking.
class MovieTicket:
    
    def __init__(self, ticket_price, quantity):
        
        self.ticket_price = ticket_price
        self.quantity = quantity

    def total_cost(self):
        
        total = self.ticket_price * self.quantity
        print("Total Cost =", total)

m = MovieTicket(200, 3)
m.total_cost()
