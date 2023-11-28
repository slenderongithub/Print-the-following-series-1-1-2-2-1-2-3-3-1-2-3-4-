#WAP to print the following series: 1/(1+2) + 2/(1+2+3) + 3/(1+2+3+4)

n=int(input("enter the number of terms: "))
s=0
m=0
t=0
for i in range(1,n+1):
    print(i,end="")
    if(i<n+1):
        print("/",end="")
        t=t+i
    for j in range(1,n+1):
            s=(j*(1+j))/2
            print(s,end="")
            if(j<n):
                print("+",end="")
            m=t+s  
    print("+",end="")
print("=",s)

        

