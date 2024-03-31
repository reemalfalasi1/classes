class TicketPricing:
    """
    Class to represent Ticket pricing
    """
    # VAT is assumed to be static and constant
    vat = 0.05

    # Using the init constructor to initialize a ticket pricing with default values for the attributes
    def __init__(self, price_adult: float = 63.0, price_child: float = 0.0, price_senior: float = 0.0,
                 student_discount: float = 0.0, group_discount: float = 0.5):
        # Default prices based on requirements
        self.__price_adult = price_adult
        self.__price_child = price_child  # Children below 18 have free tickets
        self.__price_senior = price_senior  # Seniors above 60 have free tickets
        self.__student_discount = student_discount  # Students have free tickets
        self.__group_discount = group_discount  # 50% discount for groups

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

    # Method to print the attributes
    def __str__(self):
        return (
            "Price for Adult: " + str(self.__price_adult) + "\n" +
            "Price for Child: " + str(self.__price_child) + "\n" +
            "Price for Senior: " + str(self.__price_senior) + "\n" +
            "Student Discount: " + str(self.__student_discount) + "\n" +
            "Group Discount: " + str(self.__group_discount) + "\n"
        )

# Create an instance of TicketPricing
ticket_pricing = TicketPricing()

# Print the attributes using __str__ method
print(ticket_pricing)

