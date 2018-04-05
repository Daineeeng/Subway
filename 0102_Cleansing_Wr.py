import csv
import glob
import pandas as pd


# Case00
File_List = glob.glob('C:/Users/INHA/Desktop/환경설비팀요청자료2/0.원본/대합실공조기/*.csv')
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
            result2.to_csv('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_대합실공조기/Case00/대합실공조기-%s.csv' % date)


# Case0 전체역
File_List = glob.glob('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_대합실공조기/Case00/*.csv')

# i = 0
for file in File_List :
    df = pd.read_csv(file, header=1, engine='python', index_col=0)
    # i += 1
    # print(i)
    date = df.iloc[1,0]
    date = date.replace('/','-')
    print(date)
    df.to_csv('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_대합실공조기/Case0_전체역/대합실공조기-%s.csv' % date, index=False)


# Case1 부평삼거리(55,56)
File_List = glob.glob('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_대합실공조기/Case0_전체역/*.csv')

# i = 0
for file in File_List :
    df = pd.read_csv(file, encoding='UTF-8', header=0, engine='python')
    if 'Time' in str(list(df.columns.values)) :
        df = df.loc[:,['<>Date','Time','Point_55','Point_56']]
    elif '날짜' in str(list(df.columns.values)) :
        df = df.loc[:,['<>날짜','시간','관제점_55','관제점_56']]
    # i += 1
    date = df.iloc[1,0]
    date = date.replace('/','-')
    print(date)
    df.to_csv('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_대합실공조기/Case1_부평3/Case1_대합실공조기-%s.csv' % date)


# Case2 간석오거리-동수(53-60)
File_List = glob.glob('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_대합실공조기/Case0_전체역/*.csv')

# i = 0
for file in File_List :
    df = pd.read_csv(file, encoding='UTF-8', header=0, engine='python')
    if 'Time' in str(list(df.columns.values)) :
        df = df.loc[:,['<>Date','Time','Point_53','Point_54','Point_55','Point_56','Point_57','Point_58','Point_59','Point_60']]
    elif '날짜' in str(list(df.columns.values)) :
        df = df.loc[:,['<>날짜','시간','관제점_53','관제점_54','관제점_55','관제점_56','관제점_57','관제점_58','관제점_59','관제점_60']]
    # i += 1
    date = df.iloc[1,0]
    date = date.replace('/','-')
    print(date)
    df.to_csv('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_대합실공조기/Case2_간석5_동수/Case2_대합실공조기-%s.csv' % date)


# Case3 시청-부평(39-64)
File_List = glob.glob('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_대합실공조기/Case0_전체역/*.csv')

# i = 0
for file in File_List :
    df = pd.read_csv(file, encoding='UTF-8', header=0, engine='python')
    if 'Time' in str(list(df.columns.values)) :
        df = df.loc[:,['<>Date','Time','Point_39','Point_40','Point_41','Point_42','Point_43','Point_44','Point_45','Point_46','Point_47','Point_48','Point_49','Point_50','Point_51','Point_52','Point_53','Point_54','Point_55','Point_56','Point_57','Point_58','Point_59','Point_60','Point_61','Point_62','Point_63','Point_64']]
    elif '날짜' in str(list(df.columns.values)) :
        df = df.loc[:,['<>날짜','시간','관제점_39','관제점_40','관제점_41','관제점_42','관제점_43','관제점_44','관제점_45','관제점_46','관제점_47','관제점_48','관제점_49','관제점_50','관제점_51','관제점_52','관제점_53','관제점_54','관제점_55','관제점_56','관제점_57','관제점_58','관제점_59','관제점_60','관제점_61','관제점_62','관제점_63','관제점_64']]
    # i += 1
    date = df.iloc[1,0]
    date = date.replace('/','-')
    print(date)
    df.to_csv('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_대합실공조기/Case3_시청_부평/Case3_대합실공조기-%s.csv' % date)