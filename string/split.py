def splt(str):
    arr = list(str.split(' '))
    print(arr)

splt('nina nvisd vsdnvs')


string = '''nin sinids ninvsd nindsvm\nnsdinsd insdvn nn\nnvdsinvs vsdv svd\nvnsd vsinv vnisnv vnisn'''

print(string.splitlines())


string = 'Hello 1 World 2'
vowels = ('a','e','i','o','u')
print(''.join([c for c in string if c not in vowels]))