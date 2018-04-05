import csv
import glob
import pandas as pd


# Case00
File_List = glob.glob('C:/Users/INHA/Desktop/환경설비팀요청자료2/0.원본/본선배기/*.csv')
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
            result2.to_csv('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_본선배기/Case00/본선배기-%s.csv' % date)


# Case0 전체역
File_List = glob.glob('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_본선배기/Case00/*.csv')

# i = 0
for file in File_List :
    df = pd.read_csv(file, header=1, engine='python', index_col=0)
    # i += 1
    # print(i)
    date = df.iloc[1,0]
    date = date.replace('/','-')
    print(date)
    df.to_csv('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_본선배기/Case0_전체역/본선배기-%s.csv' % date, index=False)


# Case1 부평삼거리(45-48)
File_List = glob.glob('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_본선배기/Case0_전체역/*.csv')

# i = 0
for file in File_List :
    df = pd.read_csv(file, encoding='UTF-8', header=0, engine='python')
    if 'Time' in str(list(df.columns.values)) :
        df = df.loc[:,['<>Date','Time','Point_45','Point_46','Point_47','Point_48']]
    elif '날짜' in str(list(df.columns.values)) :
        df = df.loc[:,['<>날짜','시간','관제점_45','관제점_46','관제점_47','관제점_48']]
    # i += 1
    date = df.iloc[1,0]
    date = date.replace('/','-')
    print(date)
    df.to_csv('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_본선배기/Case1_부평3/Case1_본선배기-%s.csv' % date)


# Case2 간석오거리-동수(41-52)
File_List = glob.glob('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_본선배기/Case0_전체역/*.csv')

# i = 0
for file in File_List :
    df = pd.read_csv(file, encoding='UTF-8', header=0, engine='python')
    if 'Time' in str(list(df.columns.values)) :
        df = df.loc[:,['<>Date','Time','Point_41','Point_42','Point_43','Point_44','Point_45','Point_46','Point_47','Point_48','Point_49','Point_50','Point_51','Point_52']]
    elif '날짜' in str(list(df.columns.values)) :
        df = df.loc[:,['<>날짜','시간','<>날짜','시간','관제점_41','관제점_42','관제점_43','관제점_44','관제점_45','관제점_46','관제점_47','관제점_48','관제점_49','관제점_50','관제점_51','관제점_52']]
    # i += 1
    date = df.iloc[1,0]
    date = date.replace('/','-')
    print(date)
    df.to_csv('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_본선배기/Case2_간석5_동수/Case2_본선배기-%s.csv' % date)


# Case3 시청-부평(37-56)
File_List = glob.glob('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_본선배기/Case0_전체역/*.csv')

# i = 0
for file in File_List :
    df = pd.read_csv(file, encoding='UTF-8', header=0, engine='python')
    if 'Time' in str(list(df.columns.values)) :
        df = df.loc[:,['<>Date','Time','Point_37','Point_38','Point_39','Point_40','Point_41','Point_42','Point_43','Point_44','Point_45','Point_46','Point_47','Point_48','Point_49','Point_50','Point_51','Point_52','Point_53','Point_54','Point_55','Point_56']]
    elif '날짜' in str(list(df.columns.values)) :
        df = df.loc[:,['<>날짜','시간','관제점_37','관제점_38','관제점_39','관제점_40','관제점_41','관제점_42','관제점_43','관제점_44','관제점_45','관제점_46','관제점_47','관제점_48','관제점_49','관제점_50','관제점_51','관제점_52','관제점_53','관제점_54','관제점_55','관제점_56']]
    # i += 1
    date = df.iloc[1,0]
    date = date.replace('/','-')
    print(date)
    df.to_csv('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_본선배기/Case3_시청_부평/Case3_본선배기-%s.csv' % date)