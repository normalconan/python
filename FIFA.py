import pandas
import matplotlib.pyplot as plt
df=pandas.read_csv('C:\\Riot Games\\FIFA\\data.csv')
arr=[]
for x in range(int(df.size/89)):
    if df.iloc[x][21]=='GK':
        arr.append(x)
df=df.drop(arr)



arr2=[]
for x in range(int(df.size/89)):
    str='0'
    str=str+df.iloc[x][12][1]
    if str=='00':
        pass
    elif df.iloc[x][12][2]!='K':
        str=str+df.iloc[x][12][2]
        if df.iloc[x][12][3]!='K':
            str=str+df.iloc[x][12][3]
    arr2.append(int(str))
df['wage']=None
df['wage']=arr2
import matplotlib.pyplot as plt
agewage=df.groupby('Age')['wage'].mean()
agewage.plot()
overallwage=df.groupby('Overall')['wage'].mean()
overallwage.plot()



df=pandas.read_csv('C:\\Riot Games\\FIFA\\data.csv')
df=df.iloc[0:2000]
arr=[]
for x in range(int(df.size/89)):
    if df.iloc[x][21]=='GK':
        arr.append(x)
df=df.drop(arr)
from sklearn.linear_model import LogisticRegression
arrX=[]
arrY=[]
for x in range(int(df.size/89)):
    arr3=[]
    for y in range(34):
        arr3.append(int(df.iloc[x][54+y]))
    arrX.append(arr3)
    if df.iloc[x][21]=='LB' or df.iloc[x][21]=='LWB':
        arrY.append(3)
    elif df.iloc[x][21]=='LCB':
        arrY.append(1)
    elif df.iloc[x][21]=='CB':
        arrY.append(0)
    elif df.iloc[x][21]=='RCB':
        arrY.append(2)
    elif df.iloc[x][21]=='RB' or df.iloc[x][21]=='RWB':
        arrY.append(4)
    elif df.iloc[x][21]=='LDM':
        arrY.append(6)
    elif df.iloc[x][21]=='CDM':
        arrY.append(5)
    elif df.iloc[x][21]=='RDM':
        arrY.append(7)
    elif df.iloc[x][21]=='LM':
        arrY.append(11)
    elif df.iloc[x][21]=='LCM':
        arrY.append(9)
    elif df.iloc[x][21]=='CM':
        arrY.append(8)
    elif df.iloc[x][21]=='RCM':
        arrY.append(10)
    elif df.iloc[x][21]=='RM':
        arrY.append(12)
    elif df.iloc[x][21]=='LAM':
        arrY.append(14)
    elif df.iloc[x][21]=='CAM':
        arrY.append(13)
    elif df.iloc[x][21]=='RAM':
        arrY.append(15)
    elif df.iloc[x][21]=='LW':
        arrY.append(19)
    elif df.iloc[x][21]=='LS':
        arrY.append(17)
    elif df.iloc[x][21]=='ST':
        arrY.append(16)
    elif df.iloc[x][21]=='RS':
        arrY.append(18)
    elif df.iloc[x][21]=='RW':
        arrY.append(20)
    elif df.iloc[x][21]=='LF':
        arrY.append(22)
    elif df.iloc[x][21]=='CF':
        arrY.append(21)
    elif df.iloc[x][21]=='RF':
        arrY.append(23)
clf=LogisticRegression(random_state=0).fit(arrX,arrY)
clf.predict([arrX[0]])
a=clf.predict_proba([arrX[0]])