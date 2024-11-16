# Defining the Smartphone class
class Smartphone:
    def __init__(self, brand, model, storage, color):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.color = color

    def show_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB, Color: {self.color}"

    def call(self, number):
        return f"Calling {number}..."

# Inheriting the Smartphone class to create a SmartCamera
class SmartCamera(Smartphone):
    def __init__(self, brand, model, storage, color, camera_quality):
        super().__init__(brand, model, storage, color)
        self.camera_quality = camera_quality

    def show_info(self):
        basic_info = super().show_info()
        return f"{basic_info}, Camera Quality: {self.camera_quality}MP"

    def take_picture(self):
        return "Taking a picture..."

# Creating instances of Smartphone and SmartCamera
phone = Smartphone("Samsung", "Galaxy S21", 128, "Black")
camera_phone = SmartCamera("Apple", "iPhone 13", 256, "White", 12)

# Printing information about both devices
print(phone.show_info())  # Calling the method from Smartphone class
print(camera_phone.show_info())  # Calling the method from SmartCamera class (inherits Smartphone)
print(camera_phone.take_picture())  # Calling the method unique to SmartCamera class
