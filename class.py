# Base class: Smartphone
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.__price = price  # Encapsulated price attribute (private)

    # Getter for price
    def get_price(self):
        return self.__price

    # Setter for price (with validation)
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Price must be greater than zero!")

    # Method to display phone details
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: {self.__price}")


# Derived class: GamingSmartphone
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, price, gpu):
        super().__init__(brand, model, price)
        self.gpu = gpu

    # Overriding display_info to include GPU details
    def display_info(self):
        super().display_info()
        print(f"GPU: {self.gpu}")


# Example usage
phone1 = Smartphone("Apple", "iPhone 14", 999)
gaming_phone = GamingSmartphone("Asus", "ROG Phone 6", 799, "Adreno 730")

# Using methods
phone1.display_info()
gaming_phone.display_info()

# Accessing encapsulated attribute via getter and setter
print("\nUpdating price...")
gaming_phone.set_price(850)  # Update price
gaming_phone.display_info()
