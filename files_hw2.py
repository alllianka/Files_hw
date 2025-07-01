import os
import pprint


file_path = os.path.join(os.getcwd(), 'recipes.txt')
cook_book = {}

with open(file_path, 'r', encoding='UTF-8') as f:
    while True:
        # Чтение названия блюда
        dish_name = f.readline().strip()

        if not dish_name:
            break

        # Чтение количества ингредиентов
        ingredient_count = int(f.readline().strip())   

        # Чтение самих ингредиентов
        ingredients = []
        for _ in range(ingredient_count):
            ingredient_line = f.readline().strip()
            ingredient, quantity, unit = ingredient_line.split(' | ')
            ingredients.append({
                    'ingredient': ingredient,
                    'quantity': int(quantity),
                    'unit': unit
                })
            
        # Добавление блюда в словарь
        cook_book[dish_name] = ingredients
            
        # Пропуск пустой строки между рецептами
        f.readline()

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    
    for dish in dishes:
        if dish not in cook_book:
            print(f"Блюдо '{dish}' не найдено в книге рецептов.")
            continue
        
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient']
            measure = ingredient['unit']
            quantity = ingredient['quantity'] * person_count
            
            # Если ингредиент уже есть в списке, суммируем количество
            if ingredient_name in shop_list:
                shop_list[ingredient_name]['quantity'] += quantity
            else:
                shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
    
    return print(shop_list)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)      
            