""" Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s. """
import re
def match(s):
        like='^a(b*)$'
        if re.search(like, s):
          return 'Match'
        else:
          return('Not match')
print(match(str(input(''))))
""" Write a Python program that matches a string that has an 'a' followed by two to three 'b'. """
import re
def match(s):
        like='ab{2,3}'
        if re.search(like, s):
          return 'Match'
        else:
          return('Not match')
print(match(str(input(''))))
""" Write a Python program to find sequences of lowercase letters joined with a underscore. """
import re
def match(s):
        like='^[a-z]+_[a-z]'
        if re.search(like, s):
          return 'Match'
        else:
          return('Not match')
print(match(str(input(''))))
""" Write a Python program to find the sequences of one upper case letter followed by lower case letters. """
import re
def match(s):
        like='[A-Z]+[a-z]+$'
        if re.search(like, s):
          return 'Match'
        else:
          return('Not match')
print(match(str(input(''))))
""" Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'. """
import re
def match(s):
        like='a.*?b$'
        if re.search(like, s):
          return 'Match'
        else:
          return('Not match')
print(match(str(input(''))))
""" Write a Python program to replace all occurrences of space, comma, or dot with a colon. """
import re
s = str(input())
print(re.sub("[ ,.]", ":", s))
""" Write a python program to convert snake case string to camel case string. """
import re
def snakecamel(word):
  return ''.join(x.capitalize() or '_' for x in 
    word.split('_'))
print(snakecamel(str(input())))
""" Write a Python program to split a string at uppercase letters. """
import re
s=str(input())
print(re.findall('[A-Z][^A-Z]*', s))
""" Write a Python program to insert spaces between words starting with capital letters. """
import re
def spaces(s):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", s)
print(spaces(str(input())))
""" Write a Python program to convert a given camel case string to snake case. """
import re
def camelsnake(s):
        s = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s).lower()
print(camelsnake(str(input())))