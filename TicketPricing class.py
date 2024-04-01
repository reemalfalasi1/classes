class TicketPricing:
    """
    Class to represent Ticket pricing of the museum
    """
    vat = 0.05# VAT is assumed to be static and constant

    # Using the init constructor to initialize a ticket pricing with default values for the attributes
    def __init__(self, price_adult: float = 63.0, price_child: float = 0.0, price_senior: float = 0.0,
                 student_discount: float = 0.0, group_discount: float = 0.5):
        # Default prices based on requirements
        self.__price_adult = price_adult#adults tickets are 63
        self.__price_child = price_child#children below 18 have free tickets
        self.__price_senior = price_senior  #seniors above 60 have free tickets
        self.__student_discount = student_discount  #students have free tickets
        self.__group_discount = group_discount  # there is a 50% discount for groups

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

    # calculating the discounted price based on category and group status
    def calculate_discounted_price(self, category: str, is_group: bool):
        if category.lower() == "adult":#if it is an adult
            base_price = self.__price_adult #then it would be the base price which is 63
        elif category.lower() == "child": #else if it is a child
            base_price = self.__price_child #then it would be the base price which is 0
        elif category.lower() == "senior": # else if it is a senior
            base_price = self.__price_senior #then it would be the base price which is 0
        elif category.lower() == "student": #else if it is a student
            base_price = self.__student_discount #then it would be the base price with the discount which is 0
        else:
            raise ValueError("Invalid category") #else, raise that there is a value error and the category inserted is invalid

        # Apply discount based on group status
        discount_rate = self.__group_discount if is_group else 0#If is_group is False, meaning it's not a group ticket, it assigns 0 to discount_rate.It determines whether or not a discount is applicable based on whether the ticket is for a group.
        discounted_price = base_price * (1 - discount_rate)#If is_group is True, discount_rate will be subtracted from 1, resulting in a lower price (since discount_rate represents the percentage discount).If is_group is False, discount_rate is 0, so the full base price will be used.

        # calculate the total price including VAT
        total_price = discounted_price * (1 + TicketPricing.vat)#calculates the total price by adding the VAT (Value Added Tax) to the discounted price.
        return total_price#return the total price

    # a method to print the attributes
    def __str__(self):
        return (
            "Price for Adult: " + str(self.__price_adult) + "\n" +
            "Price for Child: " + str(self.__price_child) + "\n" +
            "Price for Senior: " + str(self.__price_senior) + "\n" +
            "Student Discount: " + str(self.__student_discount) + "\n" +
            "Group Discount: " + str(self.__group_discount) + "\n"
        )

#create an instance(object) of TicketPricing
ticket_pricing = TicketPricing()

# Print the attributes using __str__ method
print(ticket_pricing)

