def solve(num):
    rev=0
    if num>0:
        rev=(rev*10)+(num%10)
        num=num/10
    else:
        return num
    return num  

if __name__ == "__main__":
    print(solve(1232))