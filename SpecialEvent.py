from datetime import date
from enum import Enum
from Ticket import Ticket

class Location(Enum):  # using an enumerator since we have limited locations in the museum which are bellow
    PERMANENT_GALLERIES = "permanent galleries"
    EXHIBITION_HALLS = "exhibition halls"
    OUTDOOR_SPACES = "outdoor spaces"


class SpecialEvent(Ticket):  # special event is a type of a ticket (it has an inheritance relationship)
    """class to represent a special event"""

    def __init__(self, ticket_id: str, purchase_date: date, visitor_id: str, price: float, event_id: str,
                 event_name: str, event_date: date, location: Location):  # initializing the SpecialEvent object with attributes
        super().__init__(ticket_id, purchase_date, visitor_id, price, event_id)
        self.__event_name = event_name  # assigning the event name
        self.__event_date = event_date  # assigning the event date
        self.__location = location  # assigning the location of the event

    # getters and setters
    def get_event_name(self):
        return self.__event_name

    def set_event_name(self, event_name: str):
        self.__event_name = event_name

    def get_event_date(self):
        return self.__event_date

    def set_event_date(self, event_date: date):
        self.__event_date = event_date

    def get_location(self):
        return self.__location

    def set_location(self, location: Location):
        self.__location = location

    def reserve_special_event(self):
        # an Implementation to reserve the special event
        pass


# Define the location using the Location enum
location = Location.EXHIBITION_HALLS

# Create an instance of SpecialEvent
special_event = SpecialEvent(
    ticket_id="SE123",
    purchase_date=date.today(),
    visitor_id="V12345",
    price=25.0,
    event_id="E456",
    event_name="Special Exhibition Opening",
    event_date=date(2024, 4, 15),
    location=location
)

# Print the details of the special event
print("Special Event Details:")
print("Ticket ID:", special_event.get_ticket_id())
print("Purchase Date:", special_event.get_purchase_date())
print("Visitor ID:", special_event.get_visitor_id())
print("Price:", special_event.get_price())
print("Event ID:", special_event.get_event_id())
print("Event Name:", special_event.get_event_name())
print("Event Date:", special_event.get_event_date())
print("Location:", special_event.get_location())

