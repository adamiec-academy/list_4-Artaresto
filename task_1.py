def is_palindrome(text):
    x = text[::-1].lower()
    y = text.lower()
    if y.replace(" ", "") != x.replace(" ", ""):
        return True
    else:
        return False
  
