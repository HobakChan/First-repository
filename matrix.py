# import random

# def newMatrix(x,y):
#    mat = []
#    minv = 0
#    maxv = 10
#    for i in range(x):
#       row = []
#       for j in range(y):
#          row.append(random.randint(minv, maxv))
#       mat.append(row)
   
#    return mat



# def printMatrix(msg,mat):
#    print(msg)
#    for i in range(len(mat)):
#       print('\t', end='')
#       row = mat[i]
#       for j in range(len(row)):
#          print(f'{mat[i][j]:4}', end=' ')
#       print()
#    return



# def scalarAdd(mat,value):
#    ret = []
#    for i in range(len(mat)):
#       row = []
#       for j in range(len(mat[i])):
#          row.append(mat[i][j]+value)
#       ret.append(row)
#    return ret


# def scalarMinus(mat,value):
#    ret = []
#    for i in range(len(mat)):
#       row = []
#       for j in range(len(mat[i])):
#          row.append(mat[i][j]-value)
#       ret.append(row)
#    return ret



# def scalarMultiply(mat,value):
#    ret = []
#    for i in range(len(mat)):
#       row = []
#       for j in range(len(mat[i])):
#          row.append(mat[i][j]*value)
#       ret.append(row)
#    return ret

# def scalarDivide(mat,value):
#    ret = []
#    for i in range(len(mat)):
#       row = []
#       for j in range(len(mat[i])):
#          row.append(mat[i][j]/value)
#       ret.append(row)
#    return ret


# def multiply(m1,m2):
#     mul = []
#     for i in range(len(m1)):
#         row = []
#         for j in range(len(m2[0])):
#             a = 0
#             for k in range(len(m2)):
#                 a += m1[i][k] * m2[k][j]
#             row.append(a)
#         mul.append(row)

#     return mul

       
# def transpose(m1):
#     row = len(m1)
#     col = len(m1[0])
#     tp = [[0 for row in range(row)] for col in range(col)]

#     for i in range(row):
#         for j in range(col):
#             tp[j][i] = m1[i][j]
        
#     return tp


# def equal(m1,m2):
#     for i in range(max(len(m1),len(m2))):  
#         for j in range(max(len(m1[0]),len(m2[0]))): 
#             if len(m1) != len(m2):
#                return "not equal"
#             if len(m1[0]) != len(m2[0]):
#                return "not equal"
#             if m1[i][j] != m2[i][j]:
#                return "not equal"
#     return "equal"


            
# def newSameMatrix(x,y,seed):
#    mat = []
#    minv = 0
#    maxv = 10
#    random.seed(seed)
#    for i in range(x):
#       row = [] 
#       for j in range(y):
#          row.append(random.randint(minv, maxv))
#       mat.append(row)
   
#    return mat

# import math

# data = [41, 32, 30, 23, 24, 32, 11, 39, 24, 46, 50, 18, 41, 14, 33, 50, 38, 25, 32, 16,
# 43, 19, 35, 22, 46, 43, 10, 22, 17, 47, 66, 48, 25, 43, 28, 31, 12, 25, 12, 48]

# max_data = max(data)
# min_data = min(data)

# no_classes = 6

# unit = 1

# W = (max_data - min_data)/no_classes
# M = math.ceil(W) 

# lb = min_value - unit / 2
# lbs = []
# ups = []
# tmp = lb

# for i in range(no_classes):
#     lbs.append(tmp)
#     ubs.append(tmp+w)
#     tmp += w

# a = 0.5

# def gubun(x):
#     return min_data - a<= x <= min_data + M - a
# def gubun2(x):
#     return min_data + M -a <=x<=min_data + 2*M  - a
# def gubun3(x):
#     return min_data + 2*M -a <=x<=min_data + 3*M - a
# def gubun4(x):
#     return min_data + 3*M -a <=x<=min_data + 4*M  - a
# def gubun5(x):
#     return min_data + 4*M -a <=x<=min_data + 5*M  - a
# def gubun6(x):
#     return min_data + 5*M -a <=x<=min_data + 6*M - a

# class1 = list((filter(gubun,data))) 
# class2 = list((filter(gubun2,data)))
# class3 = list((filter(gubun3,data)))
# class4 = list((filter(gubun4,data)))
# class5 = list((filter(gubun5,data)))
# class6 = list((filter(gubun6,data)))

# do = len(data)
# do1 = len(class1)
# do2 = len(class2)
# do3 = len(class3)
# do4 = len(class4)
# do5 = len(class5)
# do6 = len(class6)
# dolist = [do1,do2,do3,do4,do5,do6]
# max_dolist = max(dolist)

# sum = 0
# sum_sang = 0

# print("  계급\t\t계급간격\t도수\t상대도수\t누적도수\t누적상대도수\t계급값")
# for i in range(0,no_classes):
#     sum += dolist[i]
#     sum_sang += dolist[i]/do
#     print("제", i+1,"계급","   ", str(min_data+M*i-a), '~' , str(min_data+M*(i+1)-a),  
#     "\t", dolist[i],"\t", dolist[i]/do,"\t\t", sum, "\t\t",round(sum_sang,3), "\t\t",(29+20*i)/2) 


# for i in range(max_dolist, 0, -1): # 수정 max로
#    for j in range(len(dolist)):
#       if(i <= dolist[j]):
#          print(" * ", end="\t")
#       else:
#          print("  ", end="\t")
#    print()


# for c in range(1,7):
#     print((2*(min_data -a) + M*(2*c-1))/2,end="\t")

# print()
# print()

# print("최대값 : ",max_data)
# print("최소값 : ",min_data)

# import matplotlib.pyplot as plt
# import numpy as np

# plt.rcParams['font.family']='Malgun Gothic'
# plt.rcParams['axes.unicode_minus']=False

# names = ['Apple', 'Lg', 'others']
# data1 = [30, 50, 20]
# data2 = [20, 60, 20]
# data3 = [10, 70, 20]
# fig, ax = plt.subplots(figsize = (6,5))
# # ax.bar(names, data1, color = '#33FFFF', edgecolor = 'black', width = 0.25, linestyle = '-.')
# # ax.bar(names, data2, color = '#33FFFF', edgecolor = 'black', width = 0.25, linestyle = '-.')
# # ax.bar(names, data3, color = '#33FFFF', edgecolor = 'black', width = 0.25, linestyle = '-.')
# ax.set_xlabel('회사')
# ax.set_ylabel('시장점유율')
# ax.set_title('기업 시장 점유율')

# pos1 = np.arange(len(data1))
# pos2 = [x+0.25 for x in pos1]
# pos3 = [x+0.25 for x in pos2]
# # pos1= [0, 1, 2]
# # pos2 = [0+0.25, 1+0.25, 2+0.25]
# # pos3 = [0+0.25+0.25, 1+0.25+0.25, 2+0.25+0.25]
# ax.bar(pos1, data1, width=0.25, label = 'Apple', edgecolor = 'black', linestyle = '-')
# ax.bar(pos2, data2, width=0.25, label = 'Samsung', edgecolor = 'black', linestyle = '--')
# ax.bar(pos3, data3, width=0.25, label = 'others', edgecolor = 'black', linestyle = '-.')

# ax.legend()
# ax.set_xticks([0.25, 1.25, 2.25])
# tick = ['2Q/2020', '3Q/2020', '4Q/2020']
# ax.set_xticklabels(tick)
# plt.show()
# fig.savefig('a.png', transparent = True, dpi =600)


# import matplotlib.pyplot as plt
# plt.rcParams['font.family'] = 'Malgun gothic'
# plt.rcParams['axes.unicode_minus'] = False
# names = ['Apple', 'LG', 'others']
# data1 = [30, 50, 20]
# fig, ax = plt.subplots(figsize = (6, 5))
# # ax.pie(data1, labels=names, autopct = '%1.1f')
# # ax.pie(data1, labels=names, autopct = '%1.1f%%', explode = [0.1,0,0])
# fig,ax = plt.subplots(figsize = (6,5), ncols = 2)
# ax[0].pie(data1, labels = names, autopct = '%1.1f%%', explode = [0.1,0,0], radius = 1)
# # ax[1].pie(data1, labels = names, autopct = '%1.1f%%', explode = [0.1,0,0], radius = 2)

# size_Kor = [8,90,2]
# ax[1].pie(size_Kor, labels = names, autopct = '%1.1f%%')
# ax[0].set_title('Global Market Share')
# ax[1].set_title('Korea Market Share')

# plt.suptitle('Marget Shares : Global vs Korea')




 
# plt.rcParams['font.family'] = 'Malgun gothic'
# plt.rcParams['axes.unicode_minus'] = False

# names = ['Apple', 'Samsung', 'others']
# data1 = [30, 50, 20]

# fig, ax = plt.subplots(figsize = (6, 5))
# ax.plot(names, data1)



# plt.show()
# import matplotlib.pyplot as plt
# import pandas as pd
# from pandas_datareader import data as pdr
# import numpy as np


# fig.ax = plt.subplots(figsize = (6, 5))
# start_date = '2017-01-01'
# ss = '005930.KS'
# df = pdr.get_data_yahoo(ss,start=start_date)
# print(df) 

# import pandas as pd
# from pandas_datareader import data as pdr
# import matplotlib.pyplot as plt
# import numpy as np
# plt.rcParams['font.family'] = 'Malgun gothic'
# plt.rcParams['axes.unicode_minus'] = False
# start_date = '2017-01-01'
# ss='005930.KS' 
# df = pdr.get_data_yahoo(ss, start=start_date)
# fig, ax = plt.subplots(figsize = (6, 5))
# ax.hist(df.Close, bins=30, color='white', edgecolor='black')
# plt.show()

# import pandas as pd
# from pandas_datareader import data as pdr
# import matplotlib.pyplot as plt
# import numpy as np
# plt.rcParams['font.family'] = 'Malgun gothic'
# plt.rcParams['axes.unicode_minus'] = False
# fig, ax = plt.subplots(figsize=(6,5))
# data = [49.6,50.5,49.9,51.6,49.6,48.7,49.7,49.1,48.7,51.0,50.1,48.7,50.4,50.6,51.5,49.4
# ,51.1,49.8,49.8,49.0,47.2,50.4,49.1,50.5,50.9,49.8,49.6,49.3,50.5,50.2,52.0,50.7
# ,50.4,48.6,50.9,51.2,50.7,48.5,50.0,51.3,47.6,49.1,51.0,51.9,49.5,49.7,48.6,49.7
# ,48.5,48.3]
# ax.boxplot(data, vert=False)
# plt.show()

# import seaborn as sns
# import matplotlib.pyplot as plt
# data = [49.6,50.5,49.9,51.6,49.6,48.7,49.7,49.1,48.7,51.0,50.1,48.7,50.4,50.6,51.5,49.4
# ,51.1,49.8,49.8,49.0,47.2,50.4,49.1,50.5,50.9,49.8,49.6,49.3,50.5,50.2,52.0,50.7
# ,50.4,48.6,50.9,51.2,50.7,48.5,50.0,51.3,47.6,49.1,51.0,51.9,49.5,49.7,48.6,49.7
# ,48.5,48.3]
# sns.boxplot(data=data, palette="vlag")
# sns.stripplot(data=data)
# plt.show()

import pandas as pd
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.family'] = 'Malgun gothic'
plt.rcParams['axes.unicode_minus'] = False
url='https://github.com/jaypiko/tmp/raw/master/MDIS_2018_HFWS.zip'
df = pd.read_csv(url, header=None)
pure_asset = df[108]
fig, ax = plt.subplots(figsize=(6,5))
ax.boxplot(pure_asset, vert=False, sym='.', showmeans=True)
plt.show()

# import pandas as pd
# from pandas_datareader import data as pdr
# import matplotlib.pyplot as plt
# import numpy as np
# plt.rcParams['font.family'] = 'Malgun gothic'
# plt.rcParams['axes.unicode_minus'] = False
# df = pd.read_table('https://archive.ics.uci.edu/ml/machine-learningdatabases/housing/housing.data', header=None, delimiter=r'\s+')
# df.columns = ['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis', 'rad',
# 'tax', 'ptratio', 'b', 'lstat', 'medv']
# fig, ax = plt.subplots(figsize=(7,7))
# ax.scatter(df.rm, df.medv, c='black', s=3)
# ax.set_xlabel('방의 갯수')
# ax.set_ylabel('주택 중위가격')
# ax.set_title('방의 갯수 대 주택중위가격 산점도', fontsize=21)
# plt.show()

print("깃허브")
