#Solution I
def revSentence(sent):
    return ''.join(list(sent.split())[::-1])


#Solution II
def revSentence1(sent):
    rev=''
    temp=''
    for i in range(len(sent)):
        if sent[i] != ' ':
            temp+=sent[i]
        else:
            rev = temp + ' ' + rev.strip()
            temp=''
    rev = temp + ' ' + rev.strip()
    return rev.strip()

     
#Driver Code
if __name__ == "__main__":
    print(revSentence1('a.b.c.d.e.f'))
    print(revSentence1('Python is not a snake, it is a language!'))
