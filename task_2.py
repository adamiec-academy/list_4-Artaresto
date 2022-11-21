def my_split(text):
    split=[]
    space = ""
    for i in text:
        if i == " ":
            split.append(space)
            space = ""
        else:
            space += i

    if space:
        split.append(space)
    return(split)
