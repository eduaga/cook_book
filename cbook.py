from pprint import pprint

cook_book = {}


def recipe_from_file(cook_book_file):
    ingr_list = []
    with open(cook_book_file, 'rt', encoding='utf-8') as meals:
        while 1:
            meal_name = meals.readline().strip()
            if not meal_name:
                break
            ingredients_count = meals.readline().strip()
            for ingredients in range(int(ingredients_count)):
                parts_list = meals.readline().strip().split(' | ')
                recipe_parts_dict = dict(ingredient_name=parts_list[0], quantity=parts_list[1], measure=parts_list[2])
                ingr_list.append(recipe_parts_dict)
            meals.readline().strip()
            cook_book[meal_name] = ingr_list
            ingr_list = []
    return cook_book


pprint(recipe_from_file('cook_book.txt'))