'''Python code to generate emails from a list of names'''

def generateEmail(names):
    email=[]
    temp='@gmail.com'
    for i in range(len(names)):
        for j in range(len(names[i])-1,-1,-1):
            if names[i][j] != ' ':
                temp=names[i][j]+temp
        email.append(temp.lower())
        temp='@gmail.com'
    return email


#Driver Code
if __name__ == "__main__":
    print(generateEmail(['Nima Yonten', 'Sangay Choden', 'Pema Norbu', 'Rangdrel Loop']))

