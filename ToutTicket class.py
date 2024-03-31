from datetime import date

# TourTicket Class (inherits from Ticket)
class TourTicket(Ticket):
    def __init__(self, ticket_id: int, purchase_date: date, visitor_id: int, price: float, event_id: int,
                 tour_date: date, group_size: int, guide_name: str):
        super().__init__(ticket_id, purchase_date, visitor_id, price, event_id)
        self.__tour_date = tour_date
        self.__group_size = group_size
        self.__guide_name = guide_name

    def get_tour_date(self):
        return self.___tour_date

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
