list_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def list_overlap():
    list_c = []  # create empty list to populate with duplicates
    for i in list_a:
        if i in list_b:
            if i not in list_c:
                list_c.append(i)
    print(list_c)

list_overlap()