

from ui import (
    show_main_menu, calculate_product_ui, search_product_ui,
    show_all_products_ui, add_product_ui, show_diary_ui
)

def main():
    """Запуск приложения"""
    while True:
        show_main_menu()
        
        choice = input("\nВыберите действие (1-6): ")
        
        if choice == "1":
            calculate_product_ui()
        elif choice == "2":
            search_product_ui()
        elif choice == "3":
            show_all_products_ui()
        elif choice == "4":
            add_product_ui()
        elif choice == "5":
            show_diary_ui()
        elif choice == "6":
            print("\nДо свидания! Будьте здоровы!")
            break
        else:
            print("\nОшибка! Выберите число от 1 до 6")

if __name__ == "__main__":
    main()