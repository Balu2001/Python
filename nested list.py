if __name__ == '__main__':
    va=[]
    bo=[]
    n=[]
    count=0
    for _ in range(int(input())):
        name = input()
        score = float(input())
        va.append(score)
        bo.append([name,score])
sova=sorted(set(va))      
sotval=sova[1]

bo.sort()
for ele in bo:
     if ele[1]==sotval:
        
        print(ele[0])       
        
