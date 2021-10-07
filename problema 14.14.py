
n=int(input('introduceti numarul de linii:'))
A=[]
if n>=2 and n<=10:
    for i in range(0,n):
        a=[]
        for j in range(0,n):
            a.append(int(input('introduceti elementele:')))
            A.append(a)
    print(A)
    dp=[]
    ds=[]
    ddp=[]
    sdp=[]           
for i in range(len(A)):
        for j in range(len(A[0])):
            if i==j:
                dp.append(A[i][j])
            if j+i==4:
                ds.append(A[i][j])
            if i>j:
                ddp.append(A[i][j])
            if i<j:
                sdp.append(A[i][j])   
print('suma elementelor pe diagonala principala:',sum(dp))
print('suma elementelor pe diagonala secundara:',sum(ds))
print('suma elementelor mai sus de diagonala principala:',sum(ddp))
print('suma elementelor mai jos de diagonala secundara:',sum(sdp))               