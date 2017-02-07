input_list = [-4,99,2,-34,76,109]

def second_largest(input_list):
    i = 0
    best_so_far = second_best = float()
    for x in input_list:
        i += 1
        if x > second_best:
            if x >= best_so_far:
                best_so_far, second_best = x, best_so_far            
            else:
                second_best = x
    return second_best if i >= 2 else None
