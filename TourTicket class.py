from datetime import date
from Ticket import Ticket
class TourTicket(Ticket):
    """ class to represent a tour ticket"""
    def __init__(self, ticket_id: str, purchase_date: date, visitor_id: str, price: float, event_id: str,
                 tour_date: date, group_size: int, guide_name: str):
        super().__init__(ticket_id, purchase_date, visitor_id, price, event_id)
        self.__tour_date = tour_date
        self.__group_size = group_size
        self.__guide_name = guide_name

    # getters and setters
    def get_tour_date(self):
        return self.__tour_date

    def set_tour_date(self, tour_date: date):
        self.__tour_date = tour_date

    def get_group_size(self):
        return self.__group_size

    def set_group_size(self, group_size: int):
        self.__group_size = group_size

    def get_guide_name(self):
        return self.__guide_name

    def set_guide_name(self, guide_name: str):
        self.__guide_name = guide_name

    def print_tour_ticket_details(self):
        print(f"Ticket ID: {self.get_ticket_id()}, Date: {self.get_purchase_date()}, Price: {self.get_price()}, Tour Date: {self.__tour_date}, Group Size: {self.__group_size}, Guide Name: {self.__guide_name}")

# creating an instance of TourTicket
tour_ticket = TourTicket(ticket_id="RGT5372", purchase_date=date(2024, 3, 31), visitor_id="78419892314", price=50.0, event_id="101",
                         tour_date=date(2024, 4, 1), group_size=10, guide_name="Thomas John")

# Print the tour ticket details
tour_ticket.print_tour_ticket_details()

