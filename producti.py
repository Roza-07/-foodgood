
#база продуктов для калькулятора калорий

#Словарь с продуктами и их калорийностью на 100 грамм
products = {
    "гречка": 110,
    "рис": 130,
    "овсянка": 88,
    "курица": 165,
    "говядина": 250,
    "свинина": 320,
    "яйцо": 155,
    "творог": 120,
    "сыр": 350,
    "хлеб белый": 265,
    "хлеб черный": 210,
    "картофель": 77,
    "макароны": 130,
    "яблоко": 52,
    "банан": 89,
    "апельсин": 47,
    "молоко": 64,
    "масло сливочное": 748,
    "сахар": 387,
    "соль": 0
}

def get_calories(product_name):
    """
    Возвращает калорийность продукта на 100 грамм.
    Если продукт не найден, возвращает None.
    """
    product_name = product_name.lower().strip()
    return products.get(product_name)

def get_all_products():
    """Возвращает список всех продуктов в базе"""
    return list(products.keys())

def add_product(product_name, calories_na_100g):
    """
    Добавляет новый продукт в базу.
    product_name - название продукта 
    calories_na_100g - калорий на 100 грамм 
    """
    products[product_name.lower()] = calories_na_100g
    return True

def search_products(search_term):
    """Ищет продукты, содержащие поисковую фразу"""
    search_term = search_term.lower()
    results = []
    for name, calories in products.items():
        if search_term in name:
            results.append((name, calories))
    return results
