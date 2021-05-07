def insertion(list):
    n = len(list)
    for i in range(n):
        for j in range(i):
            if list[i] < list[j]:
                list.insert(j, list[i])
                del list[i+1]
    return list
