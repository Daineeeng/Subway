import csv
import glob
import pandas as pd


# Case00
File_List = glob.glob('C:/Users/INHA/Desktop/환경설비팀요청자료2/0.원본/본선급기/*.csv')
i = 0
for i, file in enumerate(File_List) :
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        flag = False
        result = []
        for line in reader:
            if flag is True:
                result.append(line)
            if len(line) < 1:
                flag = True
        if file in File_List :
            i += 1
            # print(i)
            result2 = pd.DataFrame(data = result[:-1])
            date = result2.iloc[1,0]
            date = date.replace('/','-')
            result2.to_csv('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_본선급기/Case00/본선급기-%s.csv' % date)


# Case0 전체역
File_List = glob.glob('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_본선급기/Case00/*.csv')

# i = 0
for file in File_List :
    df = pd.read_csv(file, header=1, engine='python', index_col=0)
    # i += 1
    # print(i)
    date = df.iloc[1,0]
    date = date.replace('/','-')
    print(date)
    df.to_csv('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_본선급기/Case0_전체역/본선급기-%s.csv' % date, index=False)


# Case1 부평삼거리(98-100)
File_List = glob.glob('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_본선급기/Case0_전체역/*.csv')

# i = 0
for file in File_List :
    df = pd.read_csv(file, encoding='UTF-8', header=0, engine='python')
    if 'Time' in str(list(df.columns.values)) :
        df = df.loc[:,['<>Date','Time','Point_98','Point_99','Point_100']]
    elif '날짜' in str(list(df.columns.values)) :
        df = df.loc[:,['<>날짜','시간','관제점_98','관제점_99','관제점_100']]
    # i += 1
    date = df.iloc[1,0]
    date = date.replace('/','-')
    print(date)
    df.to_csv('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_본선급기/Case1_부평3/Case1_본선급기-%s.csv' % date)


# Case2 간석오거리-동수(95-103)
File_List = glob.glob('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_본선급기/Case0_전체역/*.csv')

# i = 0
for file in File_List :
    df = pd.read_csv(file, encoding='UTF-8', header=0, engine='python')
    if 'Time' in str(list(df.columns.values)) :
        df = df.loc[:,['<>Date','Time','Point_95','Point_96','Point_97','Point_98','Point_99','Point_100','Point_101','Point_102','Point_103']]
    elif '날짜' in str(list(df.columns.values)) :
        df = df.loc[:,['<>날짜','시간','관제점_95','관제점_96','관제점_97','관제점_98','관제점_99','관제점_100','관제점_101','관제점_102','관제점_103']]
    # i += 1
    date = df.iloc[1,0]
    date = date.replace('/','-')
    print(date)
    df.to_csv('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_본선급기/Case2_간석5_동수/Case2_본선급기-%s.csv' % date)


# Case3 시청-부평(92-106)
File_List = glob.glob('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_본선급기/Case0_전체역/*.csv')

i = 0
for file in File_List :
    df = pd.read_csv(file, encoding='UTF-8', header=0, engine='python')
    if 'Time' in str(list(df.columns.values)) :
        df = df.loc[:,['<>Date','Time','Point_92','Point_93','Point_94','Point_95','Point_96','Point_97','Point_98','Point_99','Point_100','Point_101','Point_102','Point_103','Point_104','Point_105','Point_106']]
    elif '날짜' in str(list(df.columns.values)) :
        df = df.loc[:,['<>날짜','시간','관제점_92','관제점_93','관제점_94','관제점_95','관제점_96','관제점_97','관제점_98','관제점_99','관제점_100','관제점_101','관제점_102','관제점_103','관제점_104','관제점_105','관제점_106']]
    i += 1
    date = df.iloc[1,0]
    date = date.replace('/','-')
    print(date)
    df.to_csv('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_본선급기/Case3_시청_부평/Case3_본선급기-%s.csv' % date)