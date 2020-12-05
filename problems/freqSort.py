
#Given a string, sort it in decreasing order of its frequencies

def freqSort(string):
    dict={}
    for i in range(len(string)):
        key=string[i]
        if key not in dict:
            dict[key]=1
        else:
            dict[key]+=1
    sorted_dict={}
    for j in sorted(dict, key=dict.get, reverse=True):
        sorted_dict[j] = dict[j]

    for k,v in sorted_dict.items():
        print(k*v, end='')
    print()


#Driver Code
if __name__ == "__main__":
    freqSort('aaazzzsdsdv')



