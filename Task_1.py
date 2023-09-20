def recipes(f):
    cook_book = {}
    while True:
        name_of_dishes = f.readline().strip()
        number_of_ingr = int(f.readline().strip())
        ingr_list = []
        for i in range(number_of_ingr):
            i = f.readline().strip()
            g = i.split(' | ')
            ingr_dict = {'ingredient_name': g[0], 'quantity': g[1], 'measure': g[2] }
            ingr_list.append(ingr_dict)
        cook_book[name_of_dishes] = ingr_list
        a = f.readline()

        if a == '':
            break
    return cook_book

with open('recipes.txt', encoding = 'utf-8') as f: 
    cook_book = recipes(f)
    print(f'cook_book = {cook_book}')