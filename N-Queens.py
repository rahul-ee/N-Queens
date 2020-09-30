def check(i,j,queen):
    if len(queen) == 0:
        return True
    else:
        row=[]
        col=[]
        diagonal_1=[]
        diagonal_2=[]
        for z in queen:
            row.append(z[0])
            col.append(z[1])
            diagonal_1.append(z[1]-z[0])
            diagonal_2.append(z[1]+z[0])
        if i in row or j in col or (j-i) in diagonal_1 or i+j in diagonal_2:
            return False
        return True
oot=[]
N = int(input())
if N==1:
    print(1)
else:
    if N>1 and N<4:
        print('Not possible')
    else:
        q_matrix = [[0 for _ in range(N)] for _ in range(N)]
        i=0
        j=0
        queen=[]
        rejected =[]

        while True:
            
            if check(i,j,queen) and [i,j] not in rejected:
                q_matrix[i][j] = 1
                queen.append([i,j])
                i=i+1
                j=0
                rejected=[]
                if len(queen) == N:
                    popo = queen.copy()
                    oot.append(popo)
                    
                    
                    jk = queen.pop()
                    q_matrix[jk[0]][jk[1]] = 0
                    i=i-1
                    j=jk[1]+1
                    q_matrix = [[0 for _ in range(N)] for _ in range(N)]
                    rejected=[]
                    if jk[1]==N-1:
                        i=i-1
                                   
            else:
                j=j+1
                if j>N-1:
                    if len(queen)==0:
                        break
                    r = queen.pop()
    
                    q_matrix[r[0]][r[1]] = 0
                    rejected.append(r)
                    i=r[0]
                    j=r[1]

        q_matrix = [[0 for _ in range(N)] for _ in range(N)]
        for i in oot:
            q_matrix = [['o' for _ in range(N)] for _ in range(N)]
            for j in i:
                q_matrix[j[0]][j[1]] = 'X'
            print(i)
            print()
            for i in q_matrix:
                for j in i:
                    print(j,end=' ')
                print()
            print()
            print()
