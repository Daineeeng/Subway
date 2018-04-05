import glob
import pandas as pd

############################################################################################################ 대합실공조기
# Case3
File_List = glob.glob('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_대합실공조기/Case0_전체역/*.csv')

for file in File_List:
    df = pd.read_csv(file, encoding='UTF-8', header=0, engine='python')
    if 'Time' in str(list(df.columns.values)):
        df = df.loc[:,
             ['<>Date', 'Time', 'Point_39', 'Point_40', 'Point_41', 'Point_42', 'Point_43', 'Point_44', 'Point_45',
              'Point_46', 'Point_47', 'Point_48', 'Point_49', 'Point_50', 'Point_51', 'Point_52', 'Point_53',
              'Point_54', 'Point_55', 'Point_56', 'Point_57', 'Point_58', 'Point_59', 'Point_60', 'Point_61',
              'Point_62', 'Point_63', 'Point_64']]
    elif '날짜' in str(list(df.columns.values)):
        df = df.loc[:,
             ['<>날짜', '시간', '관제점_39', '관제점_40', '관제점_41', '관제점_42', '관제점_43', '관제점_44', '관제점_45', '관제점_46', '관제점_47',
              '관제점_48', '관제점_49', '관제점_50', '관제점_51', '관제점_52', '관제점_53', '관제점_54', '관제점_55', '관제점_56', '관제점_57',
              '관제점_58', '관제점_59', '관제점_60', '관제점_61', '관제점_62', '관제점_63', '관제점_64']]

    Count_Row = df.shape[0]
    Count_Col = df.shape[1]
    i = 0
    j = -1
    value = -1

    for i in range(Count_Col):
        for j in range(Count_Row):
            if df.iloc[j, i] == 'ON':
                value = 1
                df.iloc[j, i] = value
            elif df.iloc[j, i] == 'OFF':
                value = 0
                df.iloc[j, i] = value
            elif isinstance(df.iloc[j, i], float):
                df.iloc[j, i] = value
            j += 1
        i += 1

    date = df.iloc[0,0]
    date = date.replace('/', '-')
    print(date)
    df.to_csv('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_대합실공조기/Case3_시청_부평/Case3_대합실공조기-%s.csv' % date, index=False)


############################################################################################################ 본선급기
# Case3
File_List = glob.glob('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_본선급기/Case0_전체역/*.csv')

for file in File_List:
    df = pd.read_csv(file, encoding='UTF-8', header=0, engine='python')
    if 'Time' in str(list(df.columns.values)):
        df = df.loc[:,
             ['<>Date', 'Time', 'Point_92','Point_93','Point_94','Point_95','Point_96','Point_97','Point_98','Point_99',
              'Point_100','Point_101','Point_102','Point_103','Point_104','Point_105','Point_106']]
    elif '날짜' in str(list(df.columns.values)):
        df = df.loc[:,
             ['<>날짜', '시간', '관제점_92','관제점_93','관제점_94','관제점_95','관제점_96','관제점_97','관제점_98','관제점_99',
              '관제점_100','관제점_101','관제점_102','관제점_103','관제점_104','관제점_105','관제점_106']]

    Count_Row = df.shape[0]
    Count_Col = df.shape[1]
    i = 0
    j = -1
    value = -1

    for i in range(Count_Col):
        for j in range(Count_Row):
            if df.iloc[j, i] == 'ON':
                value = 1
                df.iloc[j, i] = value
            elif df.iloc[j, i] == 'OFF':
                value = 0
                df.iloc[j, i] = value
            elif isinstance(df.iloc[j, i], float):
                df.iloc[j, i] = value
            j += 1
        i += 1

    date = df.iloc[0,0]
    date = date.replace('/', '-')
    print(date)
    df.to_csv('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_본선급기/Case3_시청_부평/Case3_본선급기-%s.csv' % date, index=False)


############################################################################################################ 본선배기
# Case3
File_List = glob.glob('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_본선배기/Case0_전체역/*.csv')

for file in File_List:
    df = pd.read_csv(file, encoding='UTF-8', header=0, engine='python')
    if 'Time' in str(list(df.columns.values)):
        df = df.loc[:,
             ['<>Date', 'Time', 'Point_37','Point_38','Point_39','Point_40','Point_41','Point_42','Point_43','Point_44',
              'Point_45','Point_46','Point_47','Point_48','Point_49','Point_50','Point_51','Point_52','Point_53','Point_54','Point_55','Point_56']]
    elif '날짜' in str(list(df.columns.values)):
        df = df.loc[:,
             ['<>날짜', '시간', '관제점_37','관제점_38','관제점_39','관제점_40','관제점_41','관제점_42','관제점_43','관제점_44',
              '관제점_45','관제점_46','관제점_47','관제점_48','관제점_49','관제점_50','관제점_51','관제점_52','관제점_53','관제점_54','관제점_55','관제점_56']]

    Count_Row = df.shape[0]
    Count_Col = df.shape[1]
    i = 0
    j = -1
    value = -1

    for i in range(Count_Col):
        for j in range(Count_Row):
            if df.iloc[j, i] == 'ON':
                value = 1
                df.iloc[j, i] = value
            elif df.iloc[j, i] == 'OFF':
                value = 0
                df.iloc[j, i] = value
            elif isinstance(df.iloc[j, i], float):
                df.iloc[j, i] = value
            j += 1
        i += 1

    date = df.iloc[0,0]
    date = date.replace('/', '-')
    print(date)
    df.to_csv('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_본선배기/Case3_시청_부평/Case3_본선배기-%s.csv' % date, index=False)

    
############################################################################################################ 승강장급기
# Case3
File_List = glob.glob('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_승강장급기/Case0_전체역/*.csv')

for file in File_List:
    df = pd.read_csv(file, encoding='UTF-8', header=0, engine='python')
    if 'Time' in str(list(df.columns.values)):
        df = df.loc[:,
             ['<>Date', 'Time', 'Point_17','Point_18','Point_19','Point_20','Point_21','Point_22','Point_23','Point_24','Point_25','Point_26','Point_27','Point_28']]
    elif '날짜' in str(list(df.columns.values)):
        df = df.loc[:,
             ['<>날짜', '시간', '관제점_17','관제점_18','관제점_19','관제점_20','관제점_21','관제점_22','관제점_23','관제점_24','관제점_25','관제점_26','관제점_27','관제점_28']]

    Count_Row = df.shape[0]
    Count_Col = df.shape[1]
    i = 0
    j = -1
    value = -1

    for i in range(Count_Col):
        for j in range(Count_Row):
            if df.iloc[j, i] == 'ON':
                value = 1
                df.iloc[j, i] = value
            elif df.iloc[j, i] == 'OFF':
                value = 0
                df.iloc[j, i] = value
            elif isinstance(df.iloc[j, i], float):
                df.iloc[j, i] = value
            j += 1
        i += 1

    date = df.iloc[0,0]
    date = date.replace('/', '-')
    print(date)
    df.to_csv('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_승강장급기/Case3_시청_부평/Case3_승강장급기-%s.csv' % date, index=False)
    

############################################################################################################ 승공배기
# Case3
File_List = glob.glob('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_승공배기/Case0_전체역/*.csv')

for file in File_List:
    df = pd.read_csv(file, encoding='UTF-8', header=0, engine='python')
    if 'Time' in str(list(df.columns.values)):
        df = df.loc[:,
             ['<>Date', 'Time', 'Point_17','Point_18','Point_19','Point_20','Point_21','Point_22','Point_23','Point_24','Point_25','Point_26']]
    elif '날짜' in str(list(df.columns.values)):
        df = df.loc[:,
             ['<>날짜', '시간', '관제점_17','관제점_18','관제점_19','관제점_20','관제점_21','관제점_22','관제점_23','관제점_24','관제점_25','관제점_26']]

    Count_Row = df.shape[0]
    Count_Col = df.shape[1]
    i = 0
    j = -1
    value = -1

    for i in range(Count_Col):
        for j in range(Count_Row):
            if df.iloc[j, i] == 'ON':
                value = 1
                df.iloc[j, i] = value
            elif df.iloc[j, i] == 'OFF':
                value = 0
                df.iloc[j, i] = value
            elif isinstance(df.iloc[j, i], float):
                df.iloc[j, i] = value
            j += 1
        i += 1

    date = df.iloc[0,0]
    date = date.replace('/', '-')
    print(date)
    df.to_csv('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_승공배기/Case3_시청_부평/Case3_승공배기-%s.csv' % date, index=False)


############################################################################################################ 승공배기
# Case3
File_List = glob.glob('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_승공배기/Case0_전체역/*.csv')

for file in File_List:
    df = pd.read_csv(file, encoding='UTF-8', header=0, engine='python')
    if 'Time' in str(list(df.columns.values)):
        df = df.loc[:,
             ['<>Date', 'Time', 'Point_17', 'Point_18', 'Point_19', 'Point_20', 'Point_21', 'Point_22', 'Point_23',
              'Point_24', 'Point_25', 'Point_26']]
    elif '날짜' in str(list(df.columns.values)):
        df = df.loc[:,
             ['<>날짜', '시간', '관제점_17', '관제점_18', '관제점_19', '관제점_20', '관제점_21', '관제점_22', '관제점_23', '관제점_24', '관제점_25',
              '관제점_26']]

    Count_Row = df.shape[0]
    Count_Col = df.shape[1]
    i = 0
    j = -1
    value = -1

    for i in range(Count_Col):
        for j in range(Count_Row):
            if df.iloc[j, i] == 'ON':
                value = 1
                df.iloc[j, i] = value
            elif df.iloc[j, i] == 'OFF':
                value = 0
                df.iloc[j, i] = value
            elif isinstance(df.iloc[j, i], float):
                df.iloc[j, i] = value
            j += 1
        i += 1

    date = df.iloc[0, 0]
    date = date.replace('/', '-')
    print(date)
    df.to_csv('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_승공배기/Case3_시청_부평/Case3_승공배기-%s.csv' % date, index=False)

