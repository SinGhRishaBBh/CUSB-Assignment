#Python program to check whether a string is palindrome or not
def is_palindrome(s):
  
    s = s.lower()  
    s = ''.join(e for e in s if e.isalnum())  
    return s == s[::-1]  
input_string = "22"
result = is_palindrome(input_string)

if result:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
