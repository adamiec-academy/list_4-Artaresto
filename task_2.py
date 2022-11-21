def my_split(text):
    split=[]
    space = ""
    for i in text:
        if i == " ":
            split.append(space)
            space = ""
        else:
            space += i
    better_split = list(filter(None, split))
 
    return better_split 
      
