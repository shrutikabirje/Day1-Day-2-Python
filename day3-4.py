Accept data in two 3*3  matrix and calculate the sum of the matrices.


n=[[11,45,23],[5,10,15],[20,30,50]]
b=[[10,11,12],[13,14,15],[16,17,18]]
t=[[0,0,0],[0,0,0],[0,0,0]]
for i in range (len(n)):
    for j in range (len(n[0])):
        t[i][j]=n[i][j]+b[i][j]
for d in t:
    print(d)

