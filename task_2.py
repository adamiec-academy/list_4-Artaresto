def my_split(text):
    split=[]
    space = ""
    for i in text:
        if i == " ":
            split.append(space)
            space = ""
        else:
            space += i
   
    while '' in split:
        split.remove('')   
 
    return(split) 
      
