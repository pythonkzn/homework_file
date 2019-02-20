import copy
cook_book = {}
lines = []
dishes_list = []
dishes_dict_list = {}
space_item = []

i = 0
сount_elements = 0

with open('recipes.txt','r') as f:
    for line in f:
        lines.append(line.rstrip('\n')) #переписываем файл в список для удобства работы

for elements in lines:
    if elements.isdigit():
        cook_book[lines[i-1]] = '' #задаем ключи-названия блюд в словарь
    if elements == '':
        space_item.append(i) #номера пустых строк которые разделяют блюда
    i += 1 #количество строк в списке рецептов

j = 0

def ListToDict(num):
    ingredients_dict = {}
    list_ingredients_new = []
    res1 = lines[num].split('|')
    for val in res1:
        val = val.strip()
        list_ingredients_new.append(val)
    ingredients_dict = { 'ingridient_name':list_ingredients_new[0], 'quantity':list_ingredients_new[1], 'measure':list_ingredients_new[2]}
    return ingredients_dict

dishes_count = 0
j = 2

for dishes in cook_book:
    while j <= space_item[dishes_count]:
        if j != space_item[dishes_count]:
            dishes_list.append(ListToDict(j))
        else:
            j += 3
            dishes_count += 1
            dishes_dict_list[dishes_count] = copy.deepcopy(dishes_list)
            cook_book[dishes] = dishes_dict_list[dishes_count]
            dishes_list.clear()
            break
        j += 1


print (cook_book)
