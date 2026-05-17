#интерфейс

from producti import get_all_products, get_calories, search_products
from calculator import calculate

def print_header():
    print("+" + "-"*38 + "+")
    print(" Калькулятор калорий")
    print("+" + "-"*38 + "+")

def print_footer():
    print("+" + "-"*38 + "+")

def show_menu():
    print("\n" + "-"*40)
    print("1 - Рассчитать калории")
    print("2 - Список продуктов")
    print("3 - Поиск продукта")
    print("4 - Выход")
    print("-"*40)

def main():
    while True:
        print_header()
        show_menu()
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            print("\n  Расчет калорий")
            product = input("Введите продукт: ")
            try:
                weight = float(input("Введите вес (граммы): "))
                calories, error = calculate(product, weight)
                
                if error:
                    print("\n[ОШИБКА] " + error)
                else:
                    print("\n[РЕЗУЛЬТАТ]")
                    print(" " + product + " (" + str(weight) + " г) -> " + str(calories) + " ккал")
            except ValueError:
                print("\n[ОШИБКА] Вес должен быть числом")
        
        elif choice == "2":
            print("\n  Список продуктов")
            products = get_all_products()
            for i, p in enumerate(products, 1):
                kcal = get_calories(p)
                print(" " + str(i) + ". " + p + " - " + str(kcal) + " ккал/100г")
        
        elif choice == "3":
            print("\n поиск продукта")
            search = input("Введите часть названия: ")
            results = search_products(search)
            if results:
                print("\n[НАЙДЕНО]")
                for name, kcal in results:
                    print(" " + name + " - " + str(kcal) + " ккал/100г")
            else:
                print("\n[НИЧЕГО НЕ НАЙДЕНО]")
        
        elif choice == "4":
            print_header()
            print("  До свидания! ")
            print_footer()
            break
        
        else:
            print("\n[ОШИБКА] Неверный выбор, попробуйте снова")
        
        input("\nНажмите Enter для продолжения...")

if __name__ == "__main__":
    main()