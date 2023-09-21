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

def get_shop_list_by_dishes(dishes, person_count):
    shop_list_by_dishes = {}
    for ingredients in dishes:
        for ingr in cook_book[ingredients]:
            quantity = int(ingr['quantity']) * person_count
            if ingr['ingredient_name'] in shop_list_by_dishes:
                shop_list_by_dishes[ingr['ingredient_name']]['quantity'] += quantity
            else:                
                shop_list_by_dishes[ingr['ingredient_name']] = {'measure': ingr['measure'], 'quantity': quantity}
        
    return shop_list_by_dishes


with open('recipes.txt', encoding = 'utf-8') as f: 
    cook_book = recipes(f)
    print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))

            