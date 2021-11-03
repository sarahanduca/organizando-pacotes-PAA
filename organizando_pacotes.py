global memo
memo = [None for i in range(20)]
def find_cost(nodes, k, min_cost):
    if(memo[k] == None):
        if k == 1:
            cost = 0
            for node in nodes:
                cost = cost + node[1] * (nodes[-1][0] - node[0])
            return cost
        else:
            for z in range(len(nodes) - k):
                current_min_cost = find_cost(nodes[:z+1], 1, min_cost) + find_cost(nodes[z+1:],k - 1, min_cost)
                memo[k] = current_min_cost
                if min_cost == None:
                    min_cost = current_min_cost
                elif current_min_cost < min_cost:
                    min_cost = current_min_cost
    return memo[k]

res1 = find_cost([(20, 1), (30, 1), (40, 1)], 1, None)
res2 = find_cost([(11, 3), (12, 2), (13, 1)], 1, None)
res3 = find_cost([(10, 15), (12, 17), (16, 18), (18, 13), (30, 10), (32, 1)], 2, None)
res4 = find_cost([(10, 15), (12, 17), (16, 18), (18, 13), (30, 10), (32, 1)], 3, None)

print(res1) #prints 30
print(res2) #prints 8
print(res3) #prints 278
print(res4) #prints 86