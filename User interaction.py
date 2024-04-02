from datetime import date
from enum import Enum
from typing import List

class TicketPricing:
    """
    Class to represent Ticket pricing of the museum
    """
    vat = 0.05  # VAT is assumed to be static and constant

    def __init__(self, price_adult: float = 63.0, price_child: float = 0.0, price_senior: float = 0.0,
                 student_discount: float = 0.0, group_discount: float = 0.5):
        self.__price_adult = price_adult
        self.__price_child = price_child
        self.__price_senior = price_senior
        self.__student_discount = student_discount
        self.__group_discount = group_discount

    def calculate_discounted_price(self, category: str, is_group: bool):
        category_prices = {
            "adult": self.__price_adult,
            "child": self.__price_child,
            "senior": self.__price_senior,
            "student": self.__student_discount
        }
        base_price = category_prices.get(category.lower(), 0)
        discount_rate = self.__group_discount if is_group else 0
        discounted_price = base_price * (1 - discount_rate)
        total_price = discounted_price * (1 + TicketPricing.vat)
        return total_price

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

    def set_student_discount(self, discount: float):
        self.__student_discount = discount

    def get_group_discount(self):
        return self.__group_discount

    def set_group_discount(self, discount: float):
        self.__group_discount = discount

class Ticket:
    """
    Class to represent a Ticket
    """
    def __init__(self, ticket_id: str, purchase_date: date, visitor_id: str, price: float, event_id: int):
        self.__ticket_id = ticket_id
        self.__purchase_date = purchase_date
        self.__visitor_id = visitor_id
        self.__price = price
        self.__event_id = event_id

    def get_ticket_id(self):
        return self.__ticket_id

    def set_ticket_id(self, ticket_id: str):
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

class Location(Enum):
    PERMANENT_GALLERIES = "permanent galleries"
    EXHIBITION_HALLS = "exhibition halls"
    OUTDOOR_SPACES = "outdoor spaces"

class SpecialEvent(Ticket):
    def __init__(self, ticket_id: str, purchase_date: date, visitor_id: str, price: float, event_id: str,
                 event_name: str, event_date: date, location: Location):
        super().__init__(ticket_id, purchase_date, visitor_id, price, event_id)
        self.__event_name = event_name
        self.__event_date = event_date
        self.__location = location

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

class Artifact:
    def __init__(self, artifact_id: int, name: str, description: str, age: str, culture: str, is_on_display: bool):
        self.__artifact_id = artifact_id
        self.__name = name
        self.__description = description
        self.__age = age
        self.__culture = culture
        self.__is_on_display = is_on_display

    def get_artifact_id(self):
        return self.__artifact_id

    def set_artifact_id(self, artifact_id: int):
        self.__artifact_id = artifact_id

    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_description(self):
        return self.__description

    def set_description(self, description: str):
        self.__description = description

    def get_age(self):
        return self.__age

    def set_age(self, age: str):
        self.__age = age

    def get_culture(self):
        return self.__culture

    def set_culture(self, culture: str):
        self.__culture = culture

    def is_on_display(self):
        return self.__is_on_display

    def set_is_on_display(self, is_on_display: bool):
        self.__is_on_display = is_on_display

class Artwork:
    def __init__(self, artwork_id: int, title: str, artist: str, year_of_creation: int, is_featured: bool):
        self.__artwork_id = artwork_id
        self.__title = title
        self.__artist = artist
        self.__year_of_creation = year_of_creation
        self.__is_featured = is_featured

    def get_artwork_id(self):
        return self.__artwork_id

    def set_artwork_id(self, artwork_id: int):
        self.__artwork_id = artwork_id

    def get_title(self):
        return self.__title

    def set_title(self, title: str):
        self.__title = title

    def get_artist(self):
        return self.__artist

    def set_artist(self, artist: str):
        self.__artist = artist

    def get_year_of_creation(self):
        return self.__year_of_creation

    def set_year_of_creation(self, year_of_creation: int):
        self.__year_of_creation = year_of_creation

    def get_is_featured(self):
        return self.__is_featured

    def set_is_featured(self, is_featured: bool):
        self.__is_featured = is_featured

class Exhibition:
    def __init__(self, exhibition_id: int, name: str, start_date: date, end_date: date, location: str):
        self.__exhibition_id = exhibition_id
        self.__name = name
        self.__start_date = start_date
        self.__end_date = end_date
        self.__location = location
        self.__artworks = []

    def get_exhibition_id(self):
        return self.__exhibition_id

    def set_exhibition_id(self, exhibition_id: int):
        self.__exhibition_id = exhibition_id

    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_start_date(self):
        return self.__start_date

    def set_start_date(self, start_date: date):
        self.__start_date = start_date

    def get_end_date(self):
        return self.__end_date

    def set_end_date(self, end_date: date):
        self.__end_date = end_date

    def get_location(self):
        return self.__location

    def set_location(self, location: str):
        self.__location = location

    def get_artworks(self):
        return self.__artworks

    def set_artworks(self, artworks: List[Artwork]):
        self.__artworks = artworks

    def add_artwork(self, artwork: Artwork):
        self.__artworks.append(artwork)

    def remove_artwork(self, artwork: Artwork):
        if artwork in self.__artworks:
            self.__artworks.remove(artwork)
            return True
        return False

class LouvreMuseum:
    def __init__(self, museum_name: str, address: str, opening_hours: str):
        self.__museum_name = museum_name
        self.__address = address
        self.__opening_hours = opening_hours
        self.__exhibitions = []
        self.__artifacts = []
        self.__special_events = []

    def get_museum_name(self):
        return self.__museum_name

    def set_museum_name(self, museum_name: str):
        self.__museum_name = museum_name

    def get_address(self):
        return self.__address

    def set_address(self, address: str):
        self.__address = address

    def get_opening_hours(self):
        return self.__opening_hours

    def set_opening_hours(self, opening_hours: str):
        self.__opening_hours = opening_hours

    def get_exhibitions(self):
        return self.__exhibitions

    def set_exhibitions(self, exhibitions: List[Exhibition]):
        self.__exhibitions = exhibitions

    def add_exhibition(self, exhibition: Exhibition):
        self.__exhibitions.append(exhibition)

    def remove_exhibition(self, exhibition: Exhibition):
        if exhibition in self.__exhibitions:
            self.__exhibitions.remove(exhibition)
            return True
        return False

    def get_artifacts(self):
        return self.__artifacts

    def set_artifacts(self, artifacts: List[Artifact]):
        self.__artifacts = artifacts

    def add_artifact(self, artifact: Artifact):
        self.__artifacts.append(artifact)

    def remove_artifact(self, artifact: Artifact):
        if artifact in self.__artifacts:
            self.__artifacts.remove(artifact)
            return True
        return False

    def get_special_events(self):
        return self.__special_events

    def set_special_events(self, special_events: List[SpecialEvent]):
        self.__special_events = special_events

    def add_special_event(self, special_event: SpecialEvent):
        self.__special_events.append(special_event)

    def remove_special_event(self, special_event: SpecialEvent):
        if special_event in self.__special_events:
            self.__special_events.remove(special_event)
            return True
        return False


def get_user_category():
    print("Please enter your category (student, group, senior, child): ")
    category = input().lower()
    if category not in ["student", "group", "senior", "child"]:
        print("Invalid category. Defaulting to 'adult'.")
        category = "adult"
    return category

def get_ticket_type():
    print("Are you going for a Special Event or a Tour Ticket? Enter 'special' or 'tour': ")
    ticket_type = input().lower()
    if ticket_type not in ["special", "tour"]:
        print("Invalid ticket type. Defaulting to 'special'.")
        ticket_type = "special"
    return ticket_type

def calculate_price(category):
    # Simplified pricing logic
    pricing = TicketPricing()
    is_group = category == "group"
    price = pricing.calculate_discounted_price(category, is_group)
    return price

def display_ticket_details(category, ticket_type, price):
    print("\nTicket Details:")
    print(f"Category: {category.title()}")
    print(f"Ticket Type: {'Special Event' if ticket_type == 'special' else 'Tour Ticket'}")
    print(f"Price: {price:.2f}")

def main():
    category = get_user_category()
    ticket_type = get_ticket_type()
    price = calculate_price(category)
    display_ticket_details(category, ticket_type, price)

if __name__ == "__main__":
    main()
