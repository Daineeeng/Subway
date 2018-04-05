import glob
import pandas as pd
import math

File_List = glob.glob('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/2.data_Combined/*.csv')

for file in File_List:
    name = file[-14:-4]
    name = name.replace('d-', '-')
    print(name)

    df = pd.read_csv(file, encoding='CP949', header=0, engine='python')
    df = df.iloc[:, 1:]

    count_row = df.shape[0]
    count_col = df.shape[1]-5
    i = 1

    for i in range(count_col):
        for j in range(count_row):
            if isinstance(df.iloc[j, i], float) is True:
                if math.isnan(df.iloc[j, i]) is True:
                    df.iloc[j, i] = df.iloc[j-1, i]
                else:
                    df.iloc[j, i] = df.iloc[j, i]
            j += 1
        i += 1
    df.to_csv('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/3.data_Filled/1월/data_Combined%s.csv' % name)
