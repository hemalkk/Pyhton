my_dict = {"name": "Cutu"}

my_dict.keys()  # Output: dict_keys(['name'])
my_dict.values()  # Output: dict_values(['Cutu'])
my_dict.items()  # Output: dict_items([('name', 'Cutu')])
my_dict.get("name")  # Output: 'Cutu'
new_data = {"age": 5}
my_dict.update(new_data)
# my_dict is now {'name': 'Cutu', 'age': 5}

my_dict = {
    "name": "Cutu",
    "species": "Cat",
    "age": 3,
    "attributes": {
        "color": "white",
        "weight": "4kg"
    }
}

my_set = {1, 2, 3}
my_set.add(4)
# my_set is now {1, 2, 3, 4}
my_set.remove(3)
# my_set is now {1, 2, 4}
my_set.clear()
# my_set is now set()
my_set = {1, 2, 4}
element = my_set.pop()
# element could be any one of 1, 2, or 4
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.union(set2)
# set3 is {1, 2, 3, 4, 5}
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.intersection(set2)
# set3 is {3}
my_set = {1, 2, 3}
my_set.add(4)
my_set.remove(2)
another_set = {3, 4, 5}
union_set = my_set.union(another_set)
intersection_set = my_set.intersection(another_set)
# my_set is {1, 3, 4}
# union_set is {1, 3, 4, 5}
# intersection_set is {3, 4}
