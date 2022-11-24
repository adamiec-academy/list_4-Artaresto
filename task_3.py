'''
def min_max(data):
    minimal = maximal = data[0]
    for number in data[1:]:
        if number < minimal:
            minimal = number
        elif number > maximal:
            maximal = number
    return [minimal, maximal]
'''

def min_max_better(data):
    sort = sorted(data)
    
    minimal_better = sort[0]
    maximal_better = sort[-1]
    
    return[minimal_better, maximal_better]
