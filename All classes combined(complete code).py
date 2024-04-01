from datetime import date
from typing import List
from enum import Enum

class TicketPricing:
    """
    Class to represent Ticket pricing
    """
    # VAT is assumed to be static and constant
    vat = 0.05

    # Using the init constructor to initialize a ticket pricing with default values for the attributes
    def __init__(self):
        # Default prices based on requirements
        self.__price_adult = 63.0
        self.__price_child = 0.0  # Children below 18 have free tickets
        self.__price_senior = 0.0  # Seniors above 60 have free tickets
        self.__student_discount = 0.0  # Students have free tickets
        self.__group_discount = 0.5  # 50% discount for groups

    # Getters and setters for ticket prices
    def get_price_adult(self):
        return self.__price_adult

    def set_price_adult(self, price: float):
        self.__price_adult = price

    def get_price_child(self):
        return self.__price_child

    def set_price_child(self, price: float):
        self.__price_child = price

    def get_price_senior(self):
        return self.__price_senior

    def set_price_senior(self, price: float):
        self.__price_senior = price

    def get_student_discount(self):
        return self.__student_discount

    def set_student_discount(self, price: float):
        self.__student_discount = price

    def get_group_discount(self):
        return self.__group_discount

    def set_group_discount(self, price: float):
        self.__group_discount = price

    # Calculate discounted price based on category and group status
    def calculate_discounted_price(self, category: str, is_group: bool) -> float:
        if category.lower() == "adult":
            base_price = self.__price_adult
        elif category.lower() == "child":
            base_price = self.__price_child
        elif category.lower() == "senior":
            base_price = self.__price_senior
        elif category.lower() == "student":
            base_price = self.__student_discount
        else:
            raise ValueError("Invalid category")

        # Apply discount based on group status
        discount_rate = self.__group_discount if is_group else 0
        discounted_price = base_price * (1 - discount_rate)

        # Calculate total price including VAT
        total_price = discounted_price * (1 + TicketPricing.vat)
        return total_price

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
        self.__ticket_pricing = TicketPricing()  # Instance of TicketPricing

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

class Artifact:
    def __init__(self, artifact_id: int, name: str, description: str, age: str, culture: str, is_on_display: bool):
        self.__artifact_id = artifact_id
        self.__name = name
        self.__description = description
        self.__age = age
        self.__culture = culture
        self.__is_on_display = is_on_display

    # getters and setters...
    def get_artifact_id(self) -> int:
        return self.__artifact_id

    def set_artifact_id(self, artifact_id: int) -> None:
        self.__artifact_id = artifact_id

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_description(self) -> str:
        return self.__description

    def set_description(self, description: str) -> None:
        self.__description = description

    def get_age(self) -> str:
        return self.__age

    def set_age(self, age: str) -> None:
        self.__age = age

    def get_culture(self) -> str:
        return self.__culture

    def set_culture(self, culture: str) -> None:
        self.__culture = culture

    def get_is_on_display(self) -> bool:
        return self.__is_on_display

    def set_is_on_display(self, is_on_display: bool) -> None:
        self.__is_on_display = is_on_display

class Artwork:
    def __init__(self, artwork_id: int, title: str, artist: str, year_of_creation: int, is_featured: bool):
        self.__artwork_id = artwork_id
        self.__title = title
        self.__artist = artist
        self.__year_of_creation = year_of_creation
        self.__is_featured = is_featured

    # getters and setters...
    def get_artwork_id(self) -> int:
        return self.__artwork_id

    def set_artwork_id(self, artwork_id: int) -> None:
        self.__artwork_id = artwork_id

    def get_title(self) -> str:
        return self.__title

    def set_title(self, title: str) -> None:
        self.__title = title

    def get_artist(self) -> str:
        return self.__artist

    def set_artist(self, artist: str) -> None:
        self.__artist = artist

    def get_year_of_creation(self) -> int:
        return self.__year_of_creation

    def set_year_of_creation(self, year_of_creation: int) -> None:
        self.__year_of_creation = year_of_creation

    def get_is_featured(self) -> bool:
        return self.__is_featured

    def set_is_featured(self, is_featured: bool) -> None:
        self.__is_featured = is_featured

class Exhibition:
    def __init__(self, exhibition_id: int, name: str, start_date: date, end_date: date, location: Location):
        self.__exhibition_id = exhibition_id
        self.__name = name
        self.__start_date = start_date
        self.__end_date = end_date
        self.__location = location
        self.__artworks = []  # Initialized as empty list

    # getters and setters...
    def get_exhibition_id(self) -> int:
        return self.__exhibition_id

    def set_exhibition_id(self, exhibition_id: int) -> None:
        self.__exhibition_id = exhibition_id

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_start_date(self) -> date:
        return self.__start_date

    def set_start_date(self, start_date: date) -> None:
        self.__start_date = start_date

    def get_end_date(self) -> date:
        return self.__end_date

    def set_end_date(self, end_date: date) -> None:
        self.__end_date = end_date

    def get_location(self) -> Location:
        return self.__location

    def set_location(self, location: Location) -> None:
        self.__location = location

    def get_artworks(self) -> List[Artwork]:
        return self.__artworks

    def set_artworks(self, artworks: List[Artwork]) -> None:
        self.__artworks = artworks

    def add_artwork(self, artwork: Artwork) -> None:
        self.__artworks.append(artwork)

    def remove_artwork(self, artwork: Artwork) -> bool:
        if artwork in self.__artworks:
            self.__artworks.remove(artwork)
            return True
        return False

class LouvreMuseum:
    def __init__(self, museum_name: str, address: str, opening_hours: str):
        self.__museum_name = museum_name
        self.__address = address
        self.__opening_hours = opening_hours
        self.__exhibitions = []  # Initialized as empty list
        self.__artifacts = []  # Initialized as empty list
        self.__special_events = []  # Initialized as empty list

    # getters and setters...
    def get_museum_name(self) -> str:
        return self.__museum_name

    def set_museum_name(self, museum_name: str) -> None:
        self.__museum_name = museum_name

    def get_address(self) -> str:
        return self.__address

    def set_address(self, address: str) -> None:
        self.__address = address

    def get_opening_hours(self) -> str:
        return self.__opening_hours

    def set_opening_hours(self, opening_hours: str) -> None:
        self.__opening_hours = opening_hours

    def get_exhibitions(self) -> List[Exhibition]:
        return self.__exhibitions

    def set_exhibitions(self, exhibitions: List[Exhibition]) -> None:
        self.__exhibitions = exhibitions

    def add_exhibition(self, exhibition: Exhibition) -> None:
        self.__exhibitions.append(exhibition)

    def remove_exhibition(self, exhibition: Exhibition) -> bool:
        if exhibition in self.__exhibitions:
            self.__exhibitions.remove(exhibition)
            return True
        return False

    def get_artifacts(self) -> List[Artifact]:
        return self.__artifacts

    def set_artifacts(self, artifacts: List[Artifact]) -> None:
        self.__artifacts = artifacts

    def add_artifact(self, artifact: Artifact) -> None:
        self.__artifacts.append(artifact)

    def remove_artifact(self, artifact: Artifact) -> bool:
        if artifact in self.__artifacts:
            self.__artifacts.remove(artifact)
            return True
        return False

    def get_special_events(self) -> List[SpecialEvent]:
        return self.__special_events

    def set_special_events(self, special_events: List[SpecialEvent]) -> None:
        self.__special_events = special_events

    def add_special_event(self, special_event: SpecialEvent) -> None:
        self.__special_events.append(special_event)

    def remove_special_event(self, special_event: SpecialEvent) -> bool:
        if special_event in self.__special_events:
            self.__special_events.remove(special_event)
            return True
        return False
