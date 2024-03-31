from enum import Enum
class Location(Enum):
    PERMANENT_GALLERIES = "permanent galleries"
    EXHIBITION_HALLS = "exhibition halls"
    OUTDOOR_SPACES = "outdoor spaces"


class SpecialEvent(Ticket):
    def __init__(self, ticket_id: int, purchase_date: date, visitor_id: int, price: float, event_id: int,
                 event_name: str, event_date: date, location: Location):
        super().__init__(ticket_id, purchase_date, visitor_id, price, event_id)
        self.__event_name = event_name
        self.__event_date = event_date
        self.__location = location

    # getters and setters...
    def get_event_name(self) -> str:
        return self.__event_name

    def set_event_name(self, event_name: str) -> None:
        self.__event_name = event_name

    def get_event_date(self) -> date:
        return self.__event_date

    def set_event_date(self, event_date: date) -> None:
        self.__event_date = event_date

    def get_location(self) -> Location:
        return self.__location

    def set_location(self, location: Location) -> None:
        self.__location = location

    def reserve_special_event(self) -> None:
        # Implementation to reserve the special event
        pass
