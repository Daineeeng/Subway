import glob
import pandas as pd

# Fdust
File_List = glob.glob('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/6.data_Reselected/*.csv')

all_df = []
for file in File_List :
    df = pd.read_csv(file, index_col=None)
    all_df.append(df)
df_final = pd.concat(all_df, axis=0, ignore_index=True)
df_final = df_final.sort_values(['Date','Point'], ascending=[True,True])
df_final.to_csv('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/7.Fdust_Final.csv', index=False)

# Report
File_List = glob.glob('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/6.data_Reselected/*.csv')

all_df = []
for file in File_List :
    df = pd.read_csv(file, index_col=None)
    all_df.append(df)
df_final = pd.concat(all_df, axis=0, ignore_index=True)
df_final = df_final.sort_values(['Date','Point'], ascending=[True,True])
df_final.to_csv('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/7.Report_Final.csv', index=False)
