'''Python program to check if a string is palindrome or not'''


#Using Slicing
def isPalindrome(str):
  return str==str[::-1]

#Iterative Method
def isPalindrome1(str):
  for i in range(int(len(str)/2)):
    if str[i] != str[int(len(str)-i-1)]:
      return False
    else:
      return True

#Using Concatenation
def isPalindrome2(str1):
  rev=''
  for i in str1:
      rev=i+rev
  if str1==rev:
      return True
  else:
      return False

if __name__ == "__main__":
    print(isPalindrome('moM'.casefold()))
    print(isPalindrome1('nsjdnJnjd'.casefold()))
    print(isPalindrome2('nsiJBJdsv'.casefold()))

