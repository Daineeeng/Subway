import csv
import glob
import pandas as pd


# Case00
File_List = glob.glob('C:/Users/INHA/Desktop/환경설비팀요청자료2/0.원본/터널미세먼지/*.csv')
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
            result2.to_csv('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_터널미세먼지/Case00/터널미세먼지-%s.csv' % date, index=False)


# Case1 부평삼거리(2)
File_List = glob.glob('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_터널미세먼지/Case00/*.csv')

# i = 0
for file in File_List :
    df = pd.read_csv(file, encoding='UTF-8', header=1, engine='python')
    if 'Time' in str(list(df.columns.values)) :
        df = df.loc[:,['<>Date','Time','Point_2']]
    elif '날짜' in str(list(df.columns.values)) :
        df = df.loc[:,['<>날짜','시간','관제점_2']]
    # i += 1
    date = df.iloc[1,0]
    date = date.replace('/','-')
    print(date)
    df.to_csv('C:/Users/INHA/Desktop/환경설비팀요청자료2/data_터널미세먼지/Case1_부평3/Case1_터널미세먼지-%s.csv' % date)
