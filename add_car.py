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


def add_car():
    print("\n=== ДОБАВЛЕНИЕ НОВОГО АВТОМОБИЛЯ ===")

    brand = input("Введите марку (например: Toyota): ").strip()
    if not brand:
        print("❌ Марка не может быть пустой!")
        return

    model = input("Введите модель (например: Camry): ").strip()
    if not model:
        print("❌ Модель не может быть пустой!")
        return

    year = input("Введите год выпуска (например: 2020): ").strip()
    if not year.isdigit() or not (1900 <= int(year) <= 2100):
        print("❌ Введите корректный год!")
        return

    price = input("Введите цену в $ (например: 25000): ").strip()
    if not price.isdigit():
        print("❌ Цена должна быть числом!")
        return

    cars = load_cars()
    new_id = max((c["id"] for c in cars), default=0) + 1
    new_car = {
        "id": new_id,
        "brand": brand,
        "model": model,
        "year": int(year),
        "price": int(price),
    }
    cars.append(new_car)
    save_cars(cars)

    print(f"\n✅ Автомобиль успешно добавлен!")
    print(f"   ID: {new_car['id']}")
    print(f"   Марка: {new_car['brand']}")
    print(f"   Модель: {new_car['model']}")
    print(f"   Год: {new_car['year']}")
    print(f"   Цена: ${new_car['price']:,}")