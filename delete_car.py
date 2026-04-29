import json
import os

DB_FILE = "cars.json"

def load_cars():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_cars(cars):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(cars, f, ensure_ascii=False, indent=2)

def delete_car():
    print("\n=== УДАЛИТЬ АВТОМОБИЛЬ ===")

    cars = load_cars()
    if not cars:
        print("❌ Список автомобилей пуст. Нечего удалять.")
        return

    print("\nСписок автомобилей:")
    for car in cars:
        print(f"  ID: {car['id']} | {car['brand']} {car['model']} ({car['year']}) — ${car['price']:,}")

    car_id = input("\nВведите ID автомобиля для удаления: ").strip()
    if not car_id.isdigit():
        print("❌ ID должен быть числом!")
        return

    car_id = int(car_id)
    car = next((c for c in cars if c["id"] == car_id), None)

    if not car:
        print(f"❌ Автомобиль с ID {car_id} не найден!")
        return

    cars = [c for c in cars if c["id"] != car_id]
    save_cars(cars)

    print(f"\n✅ Автомобиль успешно удалён!")
    print(f"   {car['brand']} {car['model']} ({car['year']}) — ${car['price']:,}")