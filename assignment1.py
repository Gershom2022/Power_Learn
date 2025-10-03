# Base class
class Smartphone:
    def __init__(self, brand, model, storage_gb, battery_percent):
        self.brand = brand
        self.model = model
        self.storage_gb = storage_gb
        self.battery_percent = battery_percent

    def make_call(self, number):
        if self.battery_percent > 0:
            print(f"Calling {number} from {self.brand} {self.model}...")
            self.battery_percent -= 1
        else:
            print("Battery dead. Please charge your phone.")

    def charge(self, amount):
        self.battery_percent = min(100, self.battery_percent + amount)
        print(f"Charged to {self.battery_percent}%")

    def __str__(self):
        return f"{self.brand} {self.model} with {self.storage_gb}GB storage, Battery: {self.battery_percent}%"


# Inherited class with extra features
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, storage_gb, battery_percent, camera_megapixels):
        super().__init__(brand, model, storage_gb, battery_percent)
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        if self.battery_percent > 0:
            print(f"Taking a photo with {self.camera_megapixels}MP camera...")
            self.battery_percent -= 2
        else:
            print("Battery dead. Cannot take photo.")

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, Camera: {self.camera_megapixels}MP"


# Example usage
phone = SmartphoneWithCamera("Samsung", "Galaxy S21", 128, 50, 64)
print(phone)
phone.make_call("123-456-7890")
phone.take_photo()
phone.charge(30)
print(phone)