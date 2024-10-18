def calculate_structure_sum(data):
    global_summ = 0
    for el in data:
        if isinstance(el, (int, float)):
            global_summ += el
        elif isinstance(el, str):
            global_summ += len(el)
        elif isinstance(el, (list, tuple, set)):
            global_summ += calculate_structure_sum(el)
        elif isinstance(el, dict):
            global_summ += calculate_structure_sum(list(el.values()))
            global_summ += calculate_structure_sum(list(el.keys()))

    return global_summ


data_structure = [
    [1, 2, 3,4,4,5],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8,'c':10}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)

print(result)