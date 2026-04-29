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

def edit_car():
    print("\n=== РЕДАКТИРОВАТЬ АВТОМОБИЛЬ ===")

    cars = load_cars()
    if not cars:
        print("❌ Список автомобилей пуст. Нечего редактировать.")
        return

    print("\nСписок автомобилей:")
    for car in cars:
        print(f"  ID: {car['id']} | {car['brand']} {car['model']} ({car['year']}) — ${car['price']:,}")

    car_id = input("\nВведите ID автомобиля для редактирования: ").strip()
    if not car_id.isdigit():
        print("❌ ID должен быть числом!")
        return

    car_id = int(car_id)
    car = next((c for c in cars if c["id"] == car_id), None)

    if not car:
        print(f"❌ Автомобиль с ID {car_id} не найден!")
        return

    print(f"\nРедактируем: {car['brand']} {car['model']} ({car['year']})")
    print("Что хотите изменить?")
    print("  1 — Марка")
    print("  2 — Модель")
    print("  3 — Год")
    print("  4 — Цена")

    choice = input("\nВаш выбор (1-4): ").strip()

    if choice == "1":
        new_value = input("Введите новую марку: ").strip()
        if not new_value:
            print("❌ Марка не может быть пустой!")
            return
        old_value = car["brand"]
        car["brand"] = new_value
        field = "Марка"

    elif choice == "2":
        new_value = input("Введите новую модель: ").strip()
        if not new_value:
            print("❌ Модель не может быть пустой!")
            return
        old_value = car["model"]
        car["model"] = new_value
        field = "Модель"

    elif choice == "3":
        new_value = input("Введите новый год: ").strip()
        if not new_value.isdigit() or not (1900 <= int(new_value) <= 2100):
            print("❌ Введите корректный год!")
            return
        old_value = car["year"]
        car["year"] = int(new_value)
        field = "Год"

    elif choice == "4":
        new_value = input("Введите новую цену: ").strip()
        if not new_value.isdigit():
            print("❌ Цена должна быть числом!")
            return
        old_value = car["price"]
        car["price"] = int(new_value)
        field = "Цена"

    else:
        print("❌ Неверный выбор!")
        return

    save_cars(cars)
    print(f"\n✅ Успешно обновлено!")
    print(f"   {field}: {old_value} → {new_value}")
    print(f"   {car['brand']} {car['model']} ({car['year']}) — ${car['price']:,}")