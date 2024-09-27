
def find_all_teams(ids):
    result = [[]]
    def find_combinations(ind, a):
        if ind == len(ids):
            return
        
        for j in range(ind, len(ids)):
            a.append(ids[ind])
            result.append(a)

            find_combinations(ind + 1, a[:])

    
    # for i in range(len(ids)):
    find_combinations(i, [])

    return sorted(result)