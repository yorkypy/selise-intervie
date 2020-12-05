string = '  string of whitespace    '
print(string.lstrip()) #=> 'string of whitespace    '
print(string.rstrip()) #=> '  string of whitespace'
print(string.strip()) #=> 'string of whitespace'


print(''.isspace()) #=> False
print(' '.isspace()) #=> True
print('   '.isspace()) #=> True
print(' the '.isspace()) #=> False

print('dog' * 3)






