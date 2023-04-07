OUTPUT_DIR = "output_data"

CATEGORIES = {
    "slow_cars": lambda car: car["hp"] < 120,
    "fast_cars": lambda car: 120 <= car["hp"] < 180,
    "sport_cars": lambda car: car["hp"] >= 180,
    "cheap_cars": lambda car: car["price"] < 1000,
    "medium_cars": lambda car: 1000 <= car["price"] < 5000,
    "expensive_cars": lambda car: car["price"] >= 5000,
}
