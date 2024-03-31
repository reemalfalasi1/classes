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
