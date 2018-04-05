import csv
import glob
import pandas as pd


# Case00
File_List = glob.glob('C:/Users/INHA/Desktop/환경설비팀요청자료2/0.원본/승공배기/*.csv')
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
            result2.to_csv('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_승공배기/Case00/승공배기-%s.csv' % date)


# Case0 전체역
File_List = glob.glob('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_승공배기/Case00/*.csv')

# i = 0
for file in File_List :
    df = pd.read_csv(file, header=1, engine='python', index_col=0)
    # i += 1
    # print(i)
    date = df.iloc[1,0]
    date = date.replace('/','-')
    df.to_csv('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_승공배기/Case0_전체역/승공배기-%s.csv' % date, index=False)


# Case1 부평삼거리(21,22)
File_List = glob.glob('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_승공배기/Case0_전체역/*.csv')

# i = 0
for file in File_List :
    df = pd.read_csv(file, encoding='UTF-8', header=0, engine='python')
    if 'Time' in str(list(df.columns.values)) :
        df = df.loc[:,['<>Date','Time','Point_21','Point_22']]
    elif '날짜' in str(list(df.columns.values)) :
        df = df.loc[:,['<>날짜','시간','관제점_21','관제점_22']]
    # i += 1
    date = df.iloc[1,0]
    date = date.replace('/','-')
    print(date)
    df.to_csv('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_승공배기/Case1_부평3/Case1_승공배기-%s.csv' % date)


# Case2 간석오거리-동수(19-24)
File_List = glob.glob('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_승공배기/Case0_전체역/*.csv')

# i = 0
for file in File_List :
    df = pd.read_csv(file, encoding='UTF-8', header=0, engine='python')
    if 'Time' in str(list(df.columns.values)) :
        df = df.loc[:,['<>Date','Time','Point_19','Point_20','Point_21','Point_22','Point_23','Point_24']]
    elif '날짜' in str(list(df.columns.values)) :
        df = df.loc[:,['<>날짜','시간','관제점_19','관제점_20','관제점_21','관제점_22','관제점_23','관제점_24']]
    # i += 1
    date = df.iloc[1,0]
    date = date.replace('/','-')
    print(date)
    df.to_csv('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_승공배기/Case2_간석5_동수/Case2_승공배기-%s.csv' % date)


# Case3 시청-부평(17-26)
File_List = glob.glob('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_승공배기/Case0_전체역/*.csv')

# i = 0
for file in File_List :
    df = pd.read_csv(file, encoding='UTF-8', header=0, engine='python')
    if 'Time' in str(list(df.columns.values)) :
        df = df.loc[:,['<>Date','Time','Point_17','Point_18','Point_19','Point_20','Point_21','Point_22','Point_23','Point_24','Point_25','Point_26']]
    elif '날짜' in str(list(df.columns.values)) :
        df = df.loc[:,['<>날짜','시간','관제점_17','관제점_18','관제점_19','관제점_20','관제점_21','관제점_22','관제점_23','관제점_24','관제점_25','관제점_26']]
    # i += 1
    date = df.iloc[1,0]
    date = date.replace('/','-')
    print(date)
    df.to_csv('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_승공배기/Case3_시청_부평/Case3_승공배기-%s.csv' % date)