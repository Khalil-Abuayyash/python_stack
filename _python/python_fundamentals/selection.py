def selection(list):
    for j in range(len(list)-1):
        min = list[j]
        min_idx = j
        for i in range(j,len(list)):
            if list[i] < min:
                min = list[i]
                min_idx = i
        list[j], list[min_idx] = list[min_idx], list[j]
    return list
