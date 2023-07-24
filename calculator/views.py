from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def calculate_view(requests, dish_get):
    servings = int(requests.GET.get('servings', 1))
    send_dish = {}
    for dish, ingredients in DATA.items():
        if dish_get == dish:
            for ing, count in ingredients.items():
                send_dish[ing] = count * servings

    context = {
        'recipe': send_dish
    }

    return render(requests, 'calculator/index.html', context)


def hello(request):
    return HttpResponse('hello from django')

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def recipe_details(request, recipe_list):
    servings = int(request.GET.get('servings', 1))
    recipe = DATA.get(recipe_list)
    recipe_description = {ingredient: amount * servings for ingredient, amount in recipe.items()}
    context = {
        'recipe': recipe_description,
    }
    return render(request, 'calculator/index.html', context)




