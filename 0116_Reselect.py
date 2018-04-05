import glob
import pandas as pd

File_List = glob.glob('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/5.data_Selected/*.csv')
for file in File_List:
    name = file[-14:-4]
    name = name.replace('d-', '-')
    print(name)


    df = pd.read_csv(file, encoding='CP949', header=0, engine='python')
    df = df.iloc[:, 1:]
    df['Point'] = 0

    count_row = df.shape[0]
    count_col = df.shape[1]

    for i in range(count_row):
        time = df.values[i,1][:3]
        if time == '00:' :
            df.iloc[i,-1] = 1
        elif time == '03:' :
            df.iloc[i,-1] = 2
        elif time == '05:':
            df.iloc[i,-1] = 3
        elif time == '06:':
            df.iloc[i,-1] = 4
        elif time == '07:':
            df.iloc[i,-1] = 5
        elif time == '08:':
            df.iloc[i,-1] = 6
        elif time == '09:':
            df.iloc[i,-1] = 7
        elif time == '10:':
            df.iloc[i,-1] = 8
        elif time == '11:':
            df.iloc[i,-1] = 9
        elif time == '13:':
            df.iloc[i,-1] = 10
        elif time == '15:':
            df.iloc[i,-1] = 11
        elif time == '19:':
            df.iloc[i,-1] = 12
        elif time == '21:' :
            df.iloc[i,-1] = 13
        elif time == '22:':
            df.iloc[i,-1] = 14
        i += 1
    df = df[df.Point != 0]

    df_meta = df.groupby('Point').first()
    df_meta = df_meta[['Date','Time']]

    df_cnt = df.groupby(df.Point).count()
    df_cnt = df_cnt.iloc[:,:-5]
    df_cnt = df_cnt.drop(['Date','Time'],1)

    df_sum = df.groupby(df.Point).sum()
    df_sum = df_sum.iloc[:, :-5]

    df_mean = df.groupby(df.Point).mean()
    df_mean = df_mean.iloc[:, -5:]

    i = 0
    j = 0
    df_col = df_sum.shape[1]
    df_row = df_sum.shape[0]

    for j in range(df_col):
        for i in range(df_row):
            if df_sum.iloc[i, j] == 0:
                df_sum.iloc[i, j] = 0
            elif df_sum.iloc[i, j] > df_cnt.iloc[i, j] / 2:
                df_sum.iloc[i, j] = 1
            elif df_sum.iloc[i, j] < df_cnt.iloc[i, j] / 2:
                df_sum.iloc[i, j] = 0
            elif df_sum.iloc[i, j] == df_cnt.iloc[i, j] / 2:
                df_sum.iloc[i, j] = 0.5
            i += 1
        j += 1

    df_new = pd.concat([df_meta, df_sum, df_mean], axis=1)
    df_new.to_csv('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/6.data_Reselected/data_Combined%s.csv' % name)