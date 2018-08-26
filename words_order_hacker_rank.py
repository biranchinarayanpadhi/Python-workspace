from collections import OrderedDict

def compute():
    n=int(input())
    
    d=OrderedDict()
    for i in range(n):
        j=input()
        if j not in d:
            d.update({j:1})
        else:
            d[j]+=1
    
    print(len(d.keys()))
    print(*d.values())

if __name__=="__main__":
    compute()