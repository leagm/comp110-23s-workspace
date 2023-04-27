""""Class Writing Practice."""

class PlaneTicket:

    departure_city: str
    arrival_city: str
    departure_time: int
    ticket_cost: float

    def __init__(self, city_a: str, city_b: str, depart: int, cost: float):
        """Initialize Plane Class."""
        self.departure_city == city_a
        self.arrival_city == city_b
        self.departure_time == depart
        self.ticket_cost == cost

    def __str__(self) -> str:
        """Visualize my ticket."""
        my_ticket_str: str = (f"Depart from {self.departure_city} at {self.departure_time}. ")
        my_ticket_str += f"Arrive at {self.arrival_city}. It costs ${self.ticket_cost}."

        return my_ticket_str
    
    def delay(self, delay_hours: int) -> None:
        """Delay departure_time by delay_hours."""
        self.departure_time += (delay_hours * 100)
        self.departure_time = self.departure_time % 2400

    def discount(self, discount: float) -> None:
        """Discount ticket_cost by discount."""
        self.ticket_cost *= (1 - discount)
    
def compare_prices(ticket_1: PlaneTicket, ticket_2: PlaneTicket) -> PlaneTicket:
    """Return the cheaper ticket."""
    if ticket_1.ticket_cost < ticket_2.ticket_cost:
        return ticket_1
    else:
        return ticket_2

my_ticket: PlaneTicket = PlaneTicket("Raleigh", "New Orleans", 1000, 85.25)
print(my_ticket)
my_ticket.delay(2)
print(my_ticket)
my_ticket.discount(.10)
second_ticket: PlaneTicket = PlaneTicket("Orlando", "San Francisco", 1100, 100.50)
print(compare_prices(my_ticket, second_ticket))
