from add_car import add_car
from delete_car import delete_car
from edit_car import edit_car
from view_cars import view_cars

def main():
    print("╔══════════════════════════════╗")
    print("║   УПРАВЛЕНИЕ АВТОМОБИЛЯМИ    ║")
    print("╚══════════════════════════════╝")

    while True:
        print("\nГлавное меню:")
        print("  1 — Добавить автомобиль")
        print("  2 — Удалить автомобиль")
        print("  3 — Редактировать автомобиль")
        print("  4 — Просмотреть все автомобили")
        print("  0 — Выход")

        choice = input("\nВаш выбор: ").strip()

        if choice == "1":
            add_car()
        elif choice == "2":
            delete_car()
        elif choice == "3":
            edit_car()
        elif choice == "4":
            view_cars()
        elif choice == "0":
            print("\nДо свидания!")
            break
        else:
            print("❌ Неверный выбор. Введите цифру от 0 до 4.")

if __name__ == "__main__":
    main()