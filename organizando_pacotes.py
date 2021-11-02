def organizando_pacotes(entry, i, n, k):
    min = 1000
    weight = 0
    if(k == 1):
        for el in entry[i:]:
            # entry -> [[x, w]]
            # el -> [x, w]
            if(el[0] < entry[n-1][0]):
                sub = entry[n-1][0] - el[0]
                weight = weight + el[1]*sub
            print(weight)
        return weight

    for z in range(1, n-1):
        result = organizando_pacotes(entry, i, z, 1) + organizando_pacotes(entry, z + 1, n, 1)
        # print(result)

        if(result < min):
            min = result
            # print(min)
    return min

# assert(organizando_pacotes([[20, 1], [30, 1], [40, 1]], 1, 3, 1), 30)

print(organizando_pacotes([[20, 1], [30, 1], [40, 1]], 0, 3, 1)) 
# print(organizando_pacotes([[11, 3], [12, 2], [13, 1]], 1, 3, 1)) 
# print(organizando_pacotes([[10, 15], [12, 17], [16, 18], [18, 13], [30, 10], [32, 1]], 1, 6, 2)) 
# print(organizando_pacotes([[10, 15], [12, 17], [16, 18], [18, 13], [30, 10], [32, 1]], 1, 6, 3)) 