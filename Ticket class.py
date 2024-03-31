from datetime import date

class Ticket:
    """
    class to represent a Ticket
    """
    # Using the init constructor to initialize a ticket with values for the attributes
    def __init__(self, ticket_id: int, purchase_date: date, visitor_id: str, price: float, event_id: int):
        self.__ticket_id = ticket_id #the ticket id
        self.__purchase_date = purchase_date#the purchase date of the ticket
        self.__visitor_id = visitor_id#the visitor emirates ID
        self.__price = price#the price of the purhased ticket
        self.__event_id = event_id#the event id

    # getters and setters
    def get_ticket_id(self):
        return self.__ticket_id

    def set_ticket_id(self, ticket_id: int):
        self.__ticket_id = ticket_id

    def get_purchase_date(self):
        return self.__purchase_date

    def set_purchase_date(self, purchase_date: date):
        self.__purchase_date = purchase_date

    def get_visitor_id(self):
        return self.__visitor_id

    def set_visitor_id(self, visitor_id: str):
        self.__visitor_id = visitor_id

    def get_price(self):
        return self.__price

    def set_price(self, price: float):
        self.__price = price

    def get_event_id(self):
        return self.__event_id

    def set_event_id(self, event_id: int):
        self.__event_id = event_id

    def calculate_final_price(self) -> float:
        # Determine the category of the ticket based on price
        category = self.__get_category()
        # Calculate the final price using TicketPricing instance
        final_price = self.__ticket_pricing.calculate_discounted_price(category, is_group=False)
        return final_price

    def __get_category(self) -> str:
        # Determine the category based on the price
        if self.__price == self.__ticket_pricing.get_price_adult():
            return "adult"
        elif self.__price == self.__ticket_pricing.get_price_child():
            return "child"
        elif self.__price == self.__ticket_pricing.get_price_senior():
            return "senior"
        elif self.__price == self.__ticket_pricing.get_student_discount():
            return "student"
        else:
            raise ValueError("Invalid ticket price")

    def print_ticket_details(self) -> None:
        print(f"Ticket ID: {self.__ticket_id}, Date: {self.__purchase_date}, Price: {self.__price}")