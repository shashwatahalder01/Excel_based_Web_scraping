import pandas as pd
import os 


def getdiff():
    a=os.path.join(os.getcwd(),'data','a.xlsx')
    b=os.path.join(os.getcwd(),'data','b.xlsx')

    sheet1 = pd.read_excel(a)
    sheet2 = pd.read_excel(b)

    c=[]
    for i,j in zip(sheet1,sheet2):      
        a,b =[],[]
        for m, n in zip(sheet1[i],sheet2[j]):
            a.append(m)
            b.append(n)
        for m, n in zip(range(len(a)), range(len(b))):
            if a[m] != b[n]:
                c.append(sheet1[i][m])
    return c;            
