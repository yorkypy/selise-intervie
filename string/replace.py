'''Python | Removing unwanted characters from string'''


def solve(s):
    bad_chars = [';', ':', '!', "*"]
    for i in bad_chars:
        s=s.replace(i,'')
    return s

def solve1(s):
    bad_chars = [';', ':', '!', "*"]
    return ''.join(i for i in s if not i in bad_chars)


def solve2(s):
    import string
    bad_chars = [';', ':', '!', "*"] 
    delete_dict = {sp_character: '' for sp_character in string.punctuation}
    delete_dict[' '] = ''
    table = str.maketrans(delete_dict)
    test_string = s.translate(table) 
    
    return str(test_string)

if __name__ == "__main__":
    print(solve('nin;nsdkn:jsdn!1!'))
    print(solve1('nin;nsdkn:jsdn!1!'))
    print(solve2('Ge;ek * s:fo ! r;Ge * e*k:s !'))

