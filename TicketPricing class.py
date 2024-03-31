class TicketPricing:
    # VAT is assumed to be static and constant
    vat = 0.05
    def __init__(self, price_adult: float, price_child: float, price_senior: float, student_discount: float, group_discount: float):
        self.__price_adult = price_adult
        self.__price_child = price_child
        self.__price_senior = price_senior
        self.__student_discount = student_discount
        self.__group_discount = group_discount

    #getters and setters
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

    def calculate_discounted_price(self, category: str, is_group: bool) -> float:
        base_price = getattr(self, f"_TicketPricing__price_{category.lower()}")
        discount_rate = self.__group_discount if is_group else 0
        discounted_price = base_price * (1 - discount_rate)
        total_price = discounted_price * (1 + TicketPricing.vat)
        return total_price

