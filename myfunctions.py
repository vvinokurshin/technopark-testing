# функция суммы строк
def sum_string(string1, string2):
    return string1 + string2

# функция возвращения заглавной буквы
def capital_letter(string):
    if ord(string[0]) > 90:
        return chr(ord(string[0]) - 32)

    return string[0]

# функция объединения множеств
def union_set(set1, set2):
    return set1.union(set2)

def intersection_set(set1, set2):
    return set1.intersection(set2)