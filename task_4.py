def info(data):
    for row in data:
        for element in row:
            print(element, end="")
        print()

def border_map(a, b):
    result = []
    for collumn in range(b):
        result_temporary = []
        for border_element in range(a):
            if collumn == 0 or collumn == b - 1:
                result_temporary.append("X")
            elif border_element == 0 or border_element == a - 1:
                result_temporary.append("X")
            else:
                result_temporary.append(".")
        result.append(result_temporary)
    
    return result
