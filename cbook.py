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


def get_shop_list_by_dishes(dishes, person_count):
    shop_dict = {}
    if set(dishes).issubset(cook_book):
        for meal in dishes:
            for recipe, ingredients in cook_book.items():
                if recipe == meal:
                    for ingredient in ingredients:
                        if ingredient['ingredient_name'] in shop_dict:
                            shop_dict[ingredient['ingredient_name']]['quantity'] += int(ingredient['quantity']) * person_count
                        else:
                            shop_dict[ingredient['ingredient_name']] = dict(measure=ingredient['measure'], quantity=int(ingredient['quantity'])*person_count)

    return shop_dict

recipe_from_file('cook_book.txt')
pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 5))

