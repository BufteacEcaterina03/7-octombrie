n=int(input('introduceti numarul de linii:'))
A=[]
matrice=[]
principal=0
secundar=0
if n>=2 and n<=10:
    for i in range(0,n):
        a=[]
        for j in range(0,n):
            a.append(int(input('introduceti elementele:')))
            A.append(a)
    dp=[]
    ds=[]
    ddp=[]
    sds=[] 
    djs=[]
    dss=[]          
for i in range(len(A)):
        for j in range(len(A[0])):
            if i==j:
                dp.append(A[i][j])
            if  ((i + j) == (n - 1)):
                ds.append(A[i][j])
            if i>j:
                ddp.append(A[i][j])
            if i<j:
                sds.append(A[i][j]) 
            if ((i+j) < (n-1)):
                dss += matrice[i][j]
            if ((i+j) > (n-1)):
                djs += matrice[i][j]          
print('suma elementelor pe diagonala principala:',sum(dp))
print('suma elementelor pe diagonala secundara:',sum(ds))
print('suma elementelor mai sus de diagonala principala:',sum(ddp))
print('suma elementelor mai jos de diagonala secundara:',sum(sds))   
print('suma componentelor care se află mai sus de diagonala secundara',sum(dss))
print('suma componentelor care se află mai jos diagonala secundara',(djs))   