"""Class models for the OOP assignment."""


class Vehicle:
    """Base class that describes a vehicle in a rental fleet."""

    def __init__(self, brand, model, year, daily_rate):
        self.brand = brand
        self.model = model
        self.year = year
        self.daily_rate = daily_rate

    def start_engine(self):
        return f"{self.brand} {self.model} engine started."

    def rental_cost(self, days):
        return self.daily_rate * days

    def vehicle_info(self):
        return f"{self.year} {self.brand} {self.model}"

    def __str__(self):
        return (
            f"{self.vehicle_info()} - Daily rate: ${self.daily_rate:.2f}"
        )


class ElectricCar(Vehicle):
    """Child class for electric cars."""

    def __init__(self, brand, model, year, daily_rate, battery_range):
        super().__init__(brand, model, year, daily_rate)
        self.battery_range = battery_range

    def start_engine(self):
        return f"{self.brand} {self.model} powers on silently."

    def charge(self):
        return f"{self.brand} {self.model} is charging to full capacity."

    def vehicle_info(self):
        return (
            f"{self.year} {self.brand} {self.model} "
            f"(range: {self.battery_range} km)"
        )


class Motorcycle(Vehicle):
    """Child class for motorcycles."""

    def __init__(self, brand, model, year, daily_rate, helmet_included):
        super().__init__(brand, model, year, daily_rate)
        self.helmet_included = helmet_included

    def start_engine(self):
        return f"{self.brand} {self.model} roars to life."

    def do_wheelie(self):
        return f"{self.brand} {self.model} performs a controlled wheelie."

    def vehicle_info(self):
        helmet_text = "helmet included" if self.helmet_included else "no helmet"
        return f"{self.year} {self.brand} {self.model} ({helmet_text})"
