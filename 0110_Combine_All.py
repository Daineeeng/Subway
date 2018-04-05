import glob
import pandas as pd
import math

all_file_path = []
all_file_path.extend(glob.glob('C:/Users/DAIN/환경설비팀요청자료2/data_대합실공조기/Case3_시청_부평역/*.csv'))
all_file_path.extend(glob.glob('C:/Users/DAIN/환경설비팀요청자료2/data_본선급기/Case3_시청_부평역/*.csv'))
all_file_path.extend(glob.glob('C:/Users/DAIN/환경설비팀요청자료2/data_본선배기/Case3_시청_부평역/*.csv'))
all_file_path.extend(glob.glob('C:/Users/DAIN/환경설비팀요청자료2/data_승강장급기/Case3_시청_부평역/*.csv'))
all_file_path.extend(glob.glob('C:/Users/DAIN/환경설비팀요청자료2/data_승공배기/Case3_시청_부평역/*.csv'))
all_file_path.extend(glob.glob('C:/Users/DAIN/환경설비팀요청자료2/data_터널미세먼지/Case1_부평3/*.csv'))
all_file_path.extend(glob.glob('C:/Users/DAIN/환경설비팀요청자료2/data_환경보고서/Case3_시청_부평역/*.csv'))


File_List = glob.glob('C:/Users/DAIN/환경설비팀요청자료2/data_대합실공조기/Case3_시청_부평역/*.csv')
days = []
i = 0
for file_name in File_List :
    day = File_List[i][-13:-4]
    days.append(day)
    i += 1

for day in days:
    day_file = []
    print(day)
    for file_path in all_file_path :
        if day in file_path :
            day_file.append(file_path)

    # print(day_file)
    # if day == '1-27-2017':
    #    exit(0)

    df1 = pd.read_csv(day_file[0], encoding='CP949', header=0, engine='python')
    df1 = df1.iloc[:, 1:]
    name = df1.iloc[0, 0]
    name = name.replace('/', '-')
    df1 = df1.set_index('Date')

    df2 = pd.read_csv(day_file[1], encoding='CP949', header=0, engine='python')
    df2 = df2.iloc[:, 1:]
    df2 = df2.set_index('Date')

    df3 = pd.read_csv(day_file[2], encoding='CP949', header=0, engine='python')
    df3 = df3.iloc[:, 1:]
    df3 = df3.set_index('Date')

    df4 = pd.read_csv(day_file[3], encoding='CP949', header=0, engine='python')
    df4 = df4.iloc[:, 1:]
    df4 = df4.set_index('Date')

    df5 = pd.read_csv(day_file[4], encoding='CP949', header=0, engine='python')
    df5 = df5.iloc[:, 1:]
    df5 = df5.set_index('Date')

    df6 = pd.read_csv(day_file[5], encoding='CP949', header=0, engine='python')
    df6 = df6.iloc[:, 1:]
    df6 = df6.set_index('Date')

    df7 = pd.read_csv(day_file[6], encoding='CP949', header=0, engine='python')
    df7 = df7.iloc[:, 1:]
    df7 = df7.set_index('Date')

    # 1 = 1+2
    Case3_df1 = df1.merge(df2, left_on='Time_Wr', right_on='Time_Tas', how='outer')
    count_row = Case3_df1.shape[0]

    for i in range(count_row) :
        time = Case3_df1.iloc[i, 0]
        if isinstance(time, float) is True :
            if math.isnan(time) is True :
                Case3_df1.iloc[i, 0] = Case3_df1.iloc[i,27]
            else :
                time = time
    Case3_df1 = Case3_df1.drop(['Time_Tas'], axis = 1)


    # 2 = 3+4
    Case3_df2 = df3.merge(df4, left_on='Time_Tae', right_on='Time_Pas', how='outer')
    count_row = Case3_df2.shape[0]

    for i in range(count_row) :
        time = Case3_df2.iloc[i, 0]
        if isinstance(time, float) is True :
            if math.isnan(time) is True :
                Case3_df2.iloc[i, 0] = Case3_df2.iloc[i,21]
            else :
                time = time
    Case3_df2 = Case3_df2.drop(['Time_Pas'], axis = 1)


    # 3 = 5+6
    Case3_df3 = df5.merge(df6, left_on='Time_Pae', right_on='Time_Fdust', how='outer')
    count_row = Case3_df3.shape[0]

    for i in range(count_row) :
        time = Case3_df3.iloc[i, 0]
        if isinstance(time, float) is True :
            if math.isnan(time) is True :
                Case3_df3.iloc[i, 0] = Case3_df3.iloc[i,11]
            else :
                time = time
    Case3_df3 = Case3_df3.drop(['Time_Fdust'], axis = 1)


    # 4 = 1+2
    Case3_df4 = Case3_df1.merge(Case3_df2, left_on='Time_Wr', right_on='Time_Tae', how='outer')
    count_row = Case3_df4.shape[0]

    for i in range(count_row) :
        time = Case3_df4.iloc[i, 0]
        if isinstance(time, float) is True :
            if math.isnan(time) is True :
                Case3_df4.iloc[i, 0] = Case3_df4.iloc[i,42]
            else :
                time = time
    Case3_df4 = Case3_df4.drop(['Time_Tae'], axis = 1)


    # 5 = 4+3
    Case3_df5 = Case3_df4.merge(Case3_df3, left_on='Time_Wr', right_on='Time_Pae', how='outer')
    count_row = Case3_df5.shape[0]

    for i in range(count_row) :
        time = Case3_df5.iloc[i, 0]
        if isinstance(time, float) is True :
            if math.isnan(time) is True :
                Case3_df5.iloc[i, 0] = Case3_df5.iloc[i,74]
            else :
                time = time
    Case3_df5 = Case3_df5.drop(['Time_Pae'], axis = 1)
    Case3_df5.rename(columns={'Time_Wr':'Time'}, inplace=True)
    Case3_df5 = Case3_df5.sort_values(by='Time', ascending=True)
    Case3_df5.to_csv('C:/Users/DAIN/환경설비팀요청자료2/data_Combined/Combined-%s.csv' % name)