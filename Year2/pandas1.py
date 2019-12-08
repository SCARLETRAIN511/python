import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def p1():
    s = pd.Series([1,3,6,np.nan,44,1])
    print(s)

def p2():
    #data frame is similar to the tables
    dates = pd.date_range('20160101', periods=6)
    df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=['a','b','c','d'])
    print(df)
    #print(df['b'])
    df1 = pd.DataFrame(np.arange(15).reshape(3,5), index= ['a','b','c'], columns=[1,2,3,4,5])
    print(type(df1))
    print(df1.dtypes)
    print(df1)
    df1T=df1.T
    print(df1T)

def p3():
    dates=pd.date_range('20190101',periods=6)
    df = pd.DataFrame(np.arange(24).reshape(6,4), index=dates, columns=['a','b','c','d'])
    #print(df[0:3])# row 0, 1, 2
    #print(df['2019-01-01':'2019-01-02'])
    #print(df.loc[:,['a','b']])
    #print(df.iloc[:,0:2])
    #print(df.iloc[1,2])
    print(df)
    print(df[df.a>8])

def p4():
    dates=pd.date_range('20190101',periods=6)
    df = pd.DataFrame(np.arange(24).reshape(6,4), index=dates, columns=['a','b','c','d'])
    df.iloc[1,2]=20
    df['F']=np.nan
    df['E']=pd.Series([1,2,3,4,5,6],index=pd.date_range('20190101',periods=6))#add an extra column
    print(df)
    
def p5():
    dates=pd.date_range('20190101',periods=6)
    df = pd.DataFrame(np.arange(24).reshape(6,4), index=dates, columns=['a','b','c','d'])
    df['E']=np.nan
    print(df.isnull())
    print(df)

def p6():
    data = pd.read_csv("tutorials/numpy&pandas/15_read_to/student.csv")
    print(type(data))
    print(data)
    data.to_pickle('student.pickle')

def concat():
    df1=pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'])
    df2=pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
    df3=pd.DataFrame(np.ones((3,4))*2, columns=['a','b','c','d'])
    res=pd.concat([df1,df2,df3],axis=0,ignore_index=True)
    print(res)

def concat2():
    df1=pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'],index=[1,2,3])
    df2=pd.DataFrame(np.ones((3,4))*1, columns=['b','c','d','e'],index=[2,3,4])
    res=pd.concat([df1,df2],axis=0,join="outer")
    res2=pd.concat([df1,df2],axis=0,join="inner")
    res3=pd.concat([df1,df2],axis=1,join_axes=[df1.index])
    res4=pd.concat([df1,df2],axis=1)
    print(res)
    print(res3)
    print(res4)

def append():
    df1=pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'],index=[1,2,3])
    df2=pd.DataFrame(np.ones((3,4))*1, columns=['b','c','d','e'],index=[2,3,4])
    res=df1.append(df2,ignore_index=True)
    print(res*5)

def merge1():
    left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                             'A': ['A0', 'A1', 'A2', 'A3'],
                             'B': ['B0', 'B1', 'B2', 'B3']})
    right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                              'C': ['C0', 'C1', 'C2', 'C3'],
                              'D': ['D0', 'D1', 'D2', 'D3']})
    res=pd.merge(left,right,on='key')
    print(res)            

def merge2():
    left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                      'key2': ['K0', 'K1', 'K0', 'K1'],
                      'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})
    right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                       'key2': ['K0', 'K0', 'K0', 'K0'],
                       'C': ['C0', 'C1', 'C2', 'C3'],
                       'D': ['D0', 'D1', 'D2', 'D3']})
    res=pd.merge(left,right, on=['key1','key2'], how="inner")
    print(res)

def pandaPlot():
    data=pd.Series(np.random.randn(1000),index=np.arange(1000))
    data.plot()
    plt.show()
    data1=pd.DataFrame(np.random.randn(1000,4),index=np.arange(1000),columns=list('ABCD'))
    print(data1)
    data1=data1.cumsum()
    data1.plot()
    plt.show()

if __name__ == "__main__":
    pandaPlot()