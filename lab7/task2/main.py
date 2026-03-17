"""Main script for demonstrating OOP concepts."""

from models import ElectricCar, Motorcycle, Vehicle


def main():
    fleet = [
        Vehicle("Toyota", "Corolla", 2020, 45.0),
        ElectricCar("Tesla", "Model 3", 2023, 90.0, 490),
        Motorcycle("Yamaha", "MT-07", 2022, 60.0, True),
    ]

    rental_days = 3

    for vehicle in fleet:
        print(vehicle)
        print(vehicle.start_engine())
        print(f"Rental cost for {rental_days} days: ${vehicle.rental_cost(rental_days):.2f}")

        if isinstance(vehicle, ElectricCar):
            print(vehicle.charge())
        elif isinstance(vehicle, Motorcycle):
            print(vehicle.do_wheelie())

        print("-" * 50)


if __name__ == "__main__":
    main()
