
from producti import get_calories

def calculate(product_name, weight_grams):
    """
    Рассчитывает калории для продукта с заданным весом.
    """
    calories_per_100g = get_calories(product_name)
    
    if calories_per_100g is None:
        return None, f"Продукт '{product_name}' не найден в базе"
    
    if weight_grams <= 0:
        return None, "Вес должен быть больше 0"
    
    result = (calories_per_100g / 100) * weight_grams
    return round(result, 1), None