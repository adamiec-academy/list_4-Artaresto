def is_palindrome(text):
    reversed = (text[::-1].lower()).replace(" ", "")
    original = (text.lower()).replace(" ", "")
    return original == reversed
  
