def containsNum(str):
    if str.isnumeric():
        return True
    else:
        False

if containsNum('122s'):
    print('Contains a number')
else:
    print('Does not contain number')


print('One1'.isalpha())
print('One'.isalpha())

print('sdnsk22'.isalnum())


print('nainsd'.startswith('a'))
print('nisdnvisnv'.endswith('v'))