import csv
import glob
import pandas as pd


# Case00
File_List = glob.glob('C:/Users/INHA/Desktop/환경설비팀요청자료2/0.원본/환경보고서/*.csv')
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
            result2.to_csv('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_환경보고서/Case00/환경보고서-%s.csv' % date)


# Case0 전체역
File_List = glob.glob('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_환경보고서/Case00/*.csv')

# i = 0
for file in File_List :
    df = pd.read_csv(file, header=1, engine='python', index_col=0)
    # i += 1
    # print(i)
    date = df.iloc[1,0]
    date = date.replace('/','-')
    df.to_csv('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_환경보고서/Case0_전체역/환경보고서-%s.csv' % date, index=False)


# Case1 부평삼거리(11)
File_List = glob.glob('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_환경보고서/Case0_전체역/*.csv')

# i = 0
for file in File_List :
    df = pd.read_csv(file, encoding='UTF-8', header=0, engine='python')
    if 'Time' in str(list(df.columns.values)) :
        df = df.loc[:,['<>Date','Time','Point_11']]
    elif '날짜' in str(list(df.columns.values)) :
        df = df.loc[:,['<>날짜','시간','관제점_11']]
    # i += 1
    date = df.iloc[1,0]
    date = date.replace('/','-')
    print(date)
    df.to_csv('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_환경보고서/Case1_부평3/Case1_환경보고서-%s.csv' % date)


# Case2 간석오거리-동수(10-12)
File_List = glob.glob('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_환경보고서/Case0_전체역/*.csv')

# i = 0
for file in File_List :
    df = pd.read_csv(file, encoding='UTF-8', header=0, engine='python')
    if 'Time' in str(list(df.columns.values)) :
        df = df.loc[:,['<>Date','Time','Point_10','Point_11','Point_12']]
    elif '날짜' in str(list(df.columns.values)) :
        df = df.loc[:,['<>날짜','시간','관제점_10','관제점_11','관제점_12']]
    # i += 1
    date = df.iloc[1,0]
    date = date.replace('/','-')
    print(date)
    df.to_csv('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_환경보고서/Case2_간석5_동수/Case2_환경보고서-%s.csv' % date)


# Case3 시청-부평(9-13)
File_List = glob.glob('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_환경보고서/Case0_전체역/*.csv')

# i = 0
for file in File_List :
    df = pd.read_csv(file, encoding='UTF-8', header=0, engine='python')
    if 'Time' in str(list(df.columns.values)) :
        df = df.loc[:,['<>Date','Time','Point_9','Point_10','Point_11','Point_12','Point_13']]
    elif '날짜' in str(list(df.columns.values)) :
        df = df.loc[:,['<>날짜','시간','관제점_9','관제점_10','관제점_11','관제점_12','관제점_13']]
    # i += 1
    date = df.iloc[1,0]
    date = date.replace('/','-')
    print(date)
    df.to_csv('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_환경보고서/Case3_시청_부평/Case3_환경보고서-%s.csv' % date)