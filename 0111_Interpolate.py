import glob
import pandas as pd

File_List = glob.glob('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/3.data_Filled/2월/data_Combined-2-2-2017.csv')

for file in File_List:
    name = file[-14:-4]
    name = name.replace('d-', '-')
    Date = name[1:]
    print(name)


    df = pd.read_csv(file, encoding='CP949', header=0, engine='python', index_col=0)
    # df = df.iloc[:, 1:]
    # print(df.head())

    df.rename(columns={'39_Wr': 'Wr1_120', '40_Wr': 'Wr2_120', '41_Wr': 'Wr3_120', '42_Wr': 'Wr4_120', '43_Wr': 'Wr5_120',
                 '44_Wr': 'Wr6_120', '45_Wr': 'Wr7_120', '46_Wr': 'Wr8_120', '47_Wr': 'Wr9_120', '48_Wr': 'Wr10_120',
                 '49_Wr': 'Wr11_120', '50_Wr': 'Wr12_120', '51_Wr': 'Wr13_120', '52_Wr': 'Wr14_120',
                 '53_Wr': 'Wr1_121', '54_Wr': 'Wr2_121',
                 '55_Wr': 'Wr1_122', '56_Wr': 'Wr2_122',
                 '57_Wr': 'Wr1_123', '58_Wr': 'Wr2_123', '59_Wr': 'Wr3_123', '60_Wr': 'Wr4_123',
                 '61_Wr': 'Wr1_124', '62_Wr': 'Wr2_124', '63_Wr': 'Wr3_124', '64_Wr': 'Wr4_124',
                 '92_Tas': 'Tas1_120', '93_Tas': 'Tas2_120', '94_Tas': 'Tas3_120',
                 '95_Tas': 'Tas1_121', '96_Tas': 'Tas2_121', '97_Tas': 'Tas3_121',
                 '98_Tas': 'Tas1_122', '99_Tas': 'Tas2_122', '100_Tas': 'Tas3_122',
                 '101_Tas': 'Tas1_123', '102_Tas': 'Tas2_123', '103_Tas': 'Tas3_123',
                 '104_Tas': 'Tas1_124', 'Tas_105': 'Tas2_124', '106_Tas': 'Tas3_124',
                 '37_Tae': 'Tae1_120', '38_Tae': 'Tae2_120', '39_Tae': 'Tae3_120', '40_Tae': 'Tae4_120',
                 '41_Tae': 'Tae1_121', '42_Tae': 'Tae2_121', '43_Tae': 'Tae3_121', '44_Tae': 'Tae4_121',
                 '45_Tae': 'Tae1_122', '46_Tae': 'Tae2_122', '47_Tae': 'Tae3_122', '48_Tae': 'Tae4_122',
                 '49_Tae': 'Tae1_123', '50_Tae': 'Tae2_123', '51_Tae': 'Tae3_123', '52_Tae': 'Tae4_123',
                 '53_Tae': 'Tae1_124', '54_Tae': 'Tae2_124', '55_Tae': 'Tae3_124', '56_Tae': 'Tae4_124',
                 '17_Pas': 'Pas1_120', '18_Pas': 'Pas2_120', '19_Pas': 'Pas3_120', '20_Pas': 'Pas4_120',
                 '21_Pas': 'Pas1_121', '22_Pas': 'Pas2_121',
                 '23_Pas': 'Pas1_122', '24_Pas': 'Pas2_122',
                 '25_Pas': 'Pas1_123', '26_Pas': 'Pas2_123',
                 '27_Pas': 'Pas1_124', '28_Pas': 'Pas2_124',
                 '17_Pae': 'Pae1_120', '18_Pae': 'Pae2_120',
                 '19_Pae': 'Pae1_121', '20_Pae': 'Pae2_121',
                 '21_Pae': 'Pae1_122', '22_Pae': 'Pae2_122',
                 '23_Pae': 'Pae1_123', '24_Pae': 'Pae2_123',
                 '25_Pae': 'Pae1_124', '26_Pae': 'Pae2_124',
                 # '2_Fdust': 'Fdust_122'
                 '9_Report': 'Report_120', '10_Report': 'Report_121', '11_Report': 'Report_122',
                 '12_Report': 'Report_123', '13_Report': 'Report_124'
                 }, inplace=True)

    count_row = df.shape[0]
    count_col = df.shape[1]

    for i in range(count_row) :
        df.iloc[i,0] = pd.to_datetime(df.iloc[i,0])
    df = df.set_index('Time')
    df.head()

    df_intp = df.interpolate(method='time')
    df_intp.reset_index(level='Time', inplace=True)
    df_intp.to_csv('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/4.data_Interpolated/data_Combined%s.csv' % name)