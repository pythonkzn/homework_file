import copy


def ListToDict(num, lines):
    ingredients_dict = {}
    list_ingredients_new = []
    res1 = lines[num].split('|')
    for val in res1:
        val = val.strip()
        list_ingredients_new.append(val)
    ingredients_dict = { 'ingridient_name':list_ingredients_new[0], 'quantity':list_ingredients_new[1], 'measure':list_ingredients_new[2]}
    return ingredients_dict

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    g = 0
    for recipe in dishes:
        while g <len(cook_book[recipe]):
            shop_list[cook_book[recipe][g]['ingridient_name']] = {'measure': cook_book[recipe][g]['measure'], 'quantity': int(cook_book[recipe][g]['quantity']) * person_count}
            g += 1
        g = 0
    print (shop_list)

def main():
    lines = []
    cook_book = {}
    dishes_list = []
    dishes_dict_list = {}
    space_item = []

    print('Решение задачи №1')
    i = 0
    сount_elements = 0

    with open('recipes.txt', 'r') as f:
        for line in f:
            lines.append(line.rstrip('\n'))  # переписываем файл в список для удобства работы

    for elements in lines:
        if elements.isdigit():
            cook_book[lines[i - 1]] = ''  # задаем ключи-названия блюд в словарь
        if elements == '':
            space_item.append(i)  # номера пустых строк которые разделяют блюда
        i += 1  # количество строк в списке рецептов

    j = 0

    dishes_count = 0 #порядковый номер блюда
    j = 2

    for dishes in cook_book:
        while j <= space_item[dishes_count]: #понимаем количество строк ингредиентов блюда за счет того что знаем порядковый номер пустой строки разделяющий блюда
            if j != space_item[dishes_count]:
                dishes_list.append(ListToDict(j, lines))  #список буфер, в который собираем ингредиенты одного блюда
            else:
                j += 3
                dishes_count += 1 #переход на следующее блюдо
                dishes_dict_list[dishes_count] = copy.deepcopy(dishes_list) #перед очищением списка буфера, делаем копию
                cook_book[dishes] = dishes_dict_list[dishes_count]
                dishes_list.clear() #при переходе на следующее блюдо очищаем список буфер
                break
            j += 1

    print(cook_book)  # вывод результата решения первой задачи
    print('Решение Задачи №2')
    input_list = ['Фахитос', 'Омлет']
    input_person_count = 2
    get_shop_list_by_dishes(input_list, input_person_count, cook_book)

main()
