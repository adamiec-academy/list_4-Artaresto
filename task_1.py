def is_palindrome(text):
    x = text[::-1].lower()
    y = text.lower()
    return y.replace(" ", "") == x.replace(" ", "")
  
