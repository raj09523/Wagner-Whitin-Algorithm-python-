Period=12
demands=[100,90,115,120,95,100,90,105,105,100,110,105]
setup_cost=118.125
carrying_cost=2.4
mat=[[0 for i in range(Period)]for j in range(Period)]#initiating an empty matrix
z=0
optimum_cost=[0]*Period
mat[0][0]=setup_cost
optimum_cost[0]=setup_cost #stores minimum value for producing demand in all the weeks prior to it 
schedule=[-1]*Period  #array to store the period index in which demand for ith period should be placed  
schedule[0]=0
for i in range(1,Period):
    mi=float("inf") #to get the ooptimum cost among all the runs
    ind=z   #index with optimum cost period
    for j in range(z,i+1):  #running from previous optimum index to current index
        v=0  #variable to store cost for each run
        if j==0:
            v+=setup_cost
        else:
            v=optimum_cost[j-1]+setup_cost
        
        for k in range(j+1,i+1):
            v+=demands[k]*(k-j)*carrying_cost
        mat[i][j]=v        
        if v<mi: 
            ind=j
            mi=v
    optimum_cost[i]=mi
    z=ind
    schedule[i]=z
output_matrix=[[0 for i in range(Period)]for j in range(Period)] #to get the transpose matrix
for i in range(Period):
    for j in range(Period):
        output_matrix[i][j]=mat[j][i]        
for i in range(Period):
    print(*output_matrix[i])
print("Minimum cost for each period:",*optimum_cost)
prodn_quantity=[0]*Period
for i in range(Period):
    prodn_quantity[schedule[i]]+=demands[i]
for i in range(Period):
    print("Production Quantity in period",i+1,"is",prodn_quantity[i])

    

