global memo
memo = {}
def find_cost(nodes, i, j, k, min_cost):
    if(memo[i][j][k]):
        if k == 1:
            cost = 0
            for node in nodes[i:j+1]:
                cost = cost + node[1] * (nodes[j][0] - node[0])
            memo[i][j][k] = cost
            
        else:
            for z in range(j - i + 1):
                current_min_cost = find_cost(nodes, i, z+i, 1, min_cost) + find_cost(nodes, z+i+1, j, k - 1, min_cost)
                memo[i][j][k] = current_min_cost
                if min_cost == None:
                    min_cost = current_min_cost
                elif current_min_cost < min_cost:
                    min_cost = current_min_cost

            return min_cost

res1 = find_cost([(20, 1), (30, 1), (40, 1)], 0, 2, 1, None)
res2 = find_cost([(11, 3), (12, 2), (13, 1)], 0, 2, 1, None)
res3 = find_cost([(10, 15), (12, 17), (16, 18), (18, 13), (30, 10), (32, 1)], 0, 5, 2, None)
res4 = find_cost([(10, 15), (12, 17), (16, 18), (18, 13), (30, 10), (32, 1)], 0, 5, 3, None)

print(res1) #prints 30
print(res2) #prints 8
print(res3) #prints 278
print(res4) #prints 86