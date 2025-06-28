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

 
pprint.pprint(cook_book)

        
        