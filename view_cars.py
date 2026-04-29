
import json
import os

DB_FILE = "cars.json"

def load_cars():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def view_cars():
    print("\n=== СПИСОК АВТОМОБИЛЕЙ ===")

    cars = load_cars()
    if not cars:
        print("❌ Список пуст. Добавьте первый автомобиль!")
        return

    print(f"\nВсего автомобилей: {len(cars)}\n")
    for car in cars:
        print("─" * 30)
        print(f"  ID:     {car['id']}")
        print(f"  Марка:  {car['brand']}")
        print(f"  Модель: {car['model']}")
        print(f"  Год:    {car['year']}")
        print(f"  Цена:   ${car['price']:,}")
    print("─" * 30)
    main
