import glob
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

Fdust = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/7.Fdust_Final.csv')
count_row = Fdust.shape[0]
Fdust['Month'] = 0
Fdust['Month'] = Fdust['Date'].str[:1]

font_name = mpl.font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

# 부평삼거리
# Fdust = Fdust[['Month', 'Date', 'Time', 'Fdust_122']]
# print('122max\n', Fdust.loc[Fdust.groupby(['Month'])['Fdust_122'].idxmax()])
# print('122min\n', Fdust.loc[Fdust.groupby(['Month'])['Fdust_122'].idxmin()])
# print('122mean\n', Fdust.groupby(Fdust.Month)['Fdust_122'].mean())

# print(Fdust.query('Month == "9" & 225 <= Fdust_122 <= 226'))
# print(Fdust.loc[Fdust['Fdust_122'] == 295.843704])


####################################################################################################################### Number
##################################################### 1+2
# Max
JanFeb_x = Fdust[Fdust['Date'].str.contains('1-26-2017')]
JanFeb_x = JanFeb_x.sort_values(by='Point', ascending=True)
JanFeb_Max = JanFeb_x.groupby(JanFeb_x.Point).mean()
JanFeb_Max = JanFeb_Max['Fdust_122']
JanFeb_Max = JanFeb_Max.to_frame()
JanFeb_Max.reset_index(level='Point', inplace=True)
# Min
JanFeb_i = Fdust[Fdust['Date'].str.contains('2-11-2017')]
JanFeb_i = JanFeb_i.sort_values(by='Point', ascending=True)
JanFeb_Min = JanFeb_i.groupby(JanFeb_i.Point).mean()
JanFeb_Min = JanFeb_Min['Fdust_122']
JanFeb_Min = JanFeb_Min.to_frame()
JanFeb_Min.reset_index(level='Point', inplace=True)
# Mean
Jan_n = Fdust[Fdust['Date'].str.contains('1-31-2017')]
Jan_n = Jan_n.sort_values(by='Point', ascending=True)
Jan_Mean = Jan_n.groupby(Jan_n.Point).mean()
Jan_Mean = Jan_Mean['Fdust_122']
Jan_Mean = Jan_Mean.to_frame()
Jan_Mean.reset_index(level='Point', inplace=True)
# Mean
Feb_n = Fdust[Fdust['Date'].str.contains('2-12-2017')]
Feb_n = Feb_n.sort_values(by='Point', ascending=True)
Feb_Mean = Feb_n.groupby(Feb_n.Point).mean()
Feb_Mean = Feb_Mean['Fdust_122']
Feb_Mean = Feb_Mean.to_frame()
Feb_Mean.reset_index(level='Point', inplace=True)

plt.figure(1, figsize=(20, 24))
plt.plot(JanFeb_Max.Point, JanFeb_Max.Fdust_122, label='Max 01-26', marker='.', ms=8, ls='-', c='r', lw=2)
plt.plot(JanFeb_Min.Point, JanFeb_Min.Fdust_122, label='Min 02-11', marker='.', ms=8, ls='-', c='b', lw=2)
plt.plot(Jan_Mean.Point, Jan_Mean.Fdust_122, label='Mean 01-31', marker='.', ms=8, ls='-', c='g', lw=2)
plt.plot(Feb_Mean.Point, Feb_Mean.Fdust_122, label='Mean 02-12', marker='.', ms=8, ls='-', c='m', lw=2)
xticks = ['[1]0:00', '[2]3:00', '[3]5:40', '[4]6:30', '[5]7:30', '[6]8:30\npeak',
          '[7]9:30', '[8]10:30', '[9]11:30', '[10]13:25', '[11]15:00', '[12]19:30', '[13]21:00', '[14]22:30']
plt.xticks(JanFeb_Max.Point, xticks, fontsize=13)
plt.grid(True, ls='--', c='lightgray')
plt.ylabel('터널 미세먼지\n')
plt.legend(fontsize=12)
plt.title('터널 미세먼지 - 부평삼거리 (1,2월)\n', fontsize=20)

###################################################### 3
# Max
Mar_x = Fdust[Fdust['Date'].str.contains('3-17-2017')]
Mar_x = Mar_x.sort_values(by='Point', ascending=True)
Mar_Max = Mar_x.groupby(Mar_x.Point).mean()
Mar_Max = Mar_Max['Fdust_122']
Mar_Max = Mar_Max.to_frame()
Mar_Max.reset_index(level='Point', inplace=True)
# Min
Mar_i = Fdust[Fdust['Date'].str.contains('3-8-2017')]
Mar_i = Mar_i.sort_values(by='Point', ascending=True)
Mar_Min = Mar_i.groupby(Mar_i.Point).mean()
Mar_Min = Mar_Min['Fdust_122']
Mar_Min = Mar_Min.to_frame()
Mar_Min.reset_index(level='Point', inplace=True)
# Mean
Mar_n = Fdust[Fdust['Date'].str.contains('3-6-2017')]
Mar_n = Mar_n.sort_values(by='Point', ascending=True)
Mar_Mean = Mar_n.groupby(Mar_n.Point).mean()
Mar_Mean = Mar_Mean['Fdust_122']
Mar_Mean = Mar_Mean.to_frame()
Mar_Mean.reset_index(level='Point', inplace=True)

plt.figure(3, figsize=(20, 24))
plt.plot(Mar_Max.Point, Mar_Max.Fdust_122, label='Max 03-17', marker='.', ms=8, ls='-', c='r', lw=2)
plt.plot(Mar_Min.Point, Mar_Min.Fdust_122, label='Min 03-08', marker='.', ms=8, ls='-', c='b', lw=2)
plt.plot(Mar_Mean.Point, Mar_Mean.Fdust_122, label='Mean 03-06', marker='.', ms=8, ls='-', c='g', lw=2)
xticks = ['[1]0:00', '[2]3:00', '[3]5:40', '[4]6:30', '[5]7:30', '[6]8:30\npeak',
          '[7]9:30', '[8]10:30', '[9]11:30', '[10]13:25', '[11]15:00', '[12]19:30', '[13]21:00', '[14]22:30']
plt.xticks(Mar_Max.Point, xticks, fontsize=13)
plt.grid(True, ls='--', c='lightgray')
plt.ylabel('터널 미세먼지\n')
plt.legend(fontsize=12)
plt.title('터널 미세먼지 - 부평삼거리 (3월)\n', fontsize=20)

###################################################### 4
# Max
Apr_x = Fdust[Fdust['Date'].str.contains('4-24-2017')]
Apr_x = Apr_x.sort_values(by='Point', ascending=True)
Apr_Max = Apr_x.groupby(Apr_x.Point).mean()
Apr_Max = Apr_Max['Fdust_122']
Apr_Max = Apr_Max.to_frame()
Apr_Max.reset_index(level='Point', inplace=True)
# Min
Apr_i = Fdust[Fdust['Date'].str.contains('4-12-2017')]
Apr_i = Apr_i.sort_values(by='Point', ascending=True)
Apr_Min = Apr_i.groupby(Apr_i.Point).mean()
Apr_Min = Apr_Min['Fdust_122']
Apr_Min = Apr_Min.to_frame()
Apr_Min.reset_index(level='Point', inplace=True)
# Mean
Apr_n = Fdust[Fdust['Date'].str.contains('4-9-2017')]
Apr_n = Apr_n.sort_values(by='Point', ascending=True)
Apr_Mean = Apr_n.groupby(Apr_n.Point).mean()
Apr_Mean = Apr_Mean['Fdust_122']
Apr_Mean = Apr_Mean.to_frame()
Apr_Mean.reset_index(level='Point', inplace=True)

plt.figure(5, figsize=(20, 24))
plt.plot(Apr_Max.Point, Apr_Max.Fdust_122, label='Max 04-24', marker='.', ms=8, ls='-', c='r', lw=2)
plt.plot(Apr_Min.Point, Apr_Min.Fdust_122, label='Min 04-12', marker='.', ms=8, ls='-', c='b', lw=2)
plt.plot(Apr_Mean.Point, Apr_Mean.Fdust_122, label='Mean 04-09', marker='.', ms=8, ls='-', c='g', lw=2)
xticks = ['[1]0:00', '[2]3:00', '[3]5:40', '[4]6:30', '[5]7:30', '[6]8:30\npeak',
          '[7]9:30', '[8]10:30', '[9]11:30', '[10]13:25', '[11]15:00', '[12]19:30', '[13]21:00', '[14]22:30']
plt.xticks(Apr_Max.Point, xticks, fontsize=13)
plt.grid(True, ls='--', c='lightgray')
plt.ylabel('터널 미세먼지\n')
plt.legend(fontsize=12)
plt.title('터널 미세먼지 - 부평삼거리 (4월)\n', fontsize=20)

###################################################### 5
# Max
May_x = Fdust[Fdust['Date'].str.contains('5-6-2017')]
May_x = May_x.sort_values(by='Point', ascending=True)
May_Max = May_x.groupby(May_x.Point).mean()
May_Max = May_Max['Fdust_122']
May_Max = May_Max.to_frame()
May_Max.reset_index(level='Point', inplace=True)
# Min
May_i = Fdust[Fdust['Date'].str.contains('5-11-2017')]
May_i = May_i.sort_values(by='Point', ascending=True)
May_Min = May_i.groupby(May_i.Point).mean()
May_Min = May_Min['Fdust_122']
May_Min = May_Min.to_frame()
May_Min.reset_index(level='Point', inplace=True)
# Mean
May_n = Fdust[Fdust['Date'].str.contains('5-10-2017')]
May_n = May_n.sort_values(by='Point', ascending=True)
May_Mean = May_n.groupby(May_n.Point).mean()
May_Mean = May_Mean['Fdust_122']
May_Mean = May_Mean.to_frame()
May_Mean.reset_index(level='Point', inplace=True)

plt.figure(7, figsize=(20, 24))
plt.plot(May_Max.Point, May_Max.Fdust_122, label='Max 05-06', marker='.', ms=8, ls='-', c='r', lw=2)
plt.plot(May_Min.Point, May_Min.Fdust_122, label='Min 05-11', marker='.', ms=8, ls='-', c='b', lw=2)
plt.plot(May_Mean.Point, May_Mean.Fdust_122, label='Mean 05-10', marker='.', ms=8, ls='-', c='g', lw=2)
xticks = ['[1]0:00', '[2]3:00', '[3]5:40', '[4]6:30', '[5]7:30', '[6]8:30\npeak',
          '[7]9:30', '[8]10:30', '[9]11:30', '[10]13:25', '[11]15:00', '[12]19:30', '[13]21:00', '[14]22:30']
plt.xticks(May_Max.Point, xticks, fontsize=13)
plt.grid(True, ls='--', c='lightgray')
plt.ylabel('터널 미세먼지\n')
plt.legend(fontsize=12)
plt.title('터널 미세먼지 - 부평삼거리 (5월)\n', fontsize=20)

###################################################### 7
# Max
Jun_x = Fdust[Fdust['Date'].str.contains('6-28-2017')]
Jun_x = Jun_x.sort_values(by='Point', ascending=True)
Jun_Max = Jun_x.groupby(Jun_x.Point).mean()
Jun_Max = Jun_Max['Fdust_122']
Jun_Max = Jun_Max.to_frame()
Jun_Max.reset_index(level='Point', inplace=True)
# Min
Jun_i = Fdust[Fdust['Date'].str.contains('6-29-2017')]
Jun_i = Jun_i.sort_values(by='Point', ascending=True)
Jun_Min = Jun_i.groupby(Jun_i.Point).mean()
Jun_Min = Jun_Min['Fdust_122']
Jun_Min = Jun_Min.to_frame()
Jun_Min.reset_index(level='Point', inplace=True)
# Mean
Jun_n = Fdust[Fdust['Date'].str.contains('6-27-2017')]
Jun_n = Jun_n.sort_values(by='Point', ascending=True)
Jun_Mean = Jun_n.groupby(Jun_n.Point).mean()
Jun_Mean = Jun_Mean['Fdust_122']
Jun_Mean = Jun_Mean.to_frame()
Jun_Mean.reset_index(level='Point', inplace=True)

plt.figure(9, figsize=(20, 24))
plt.plot(Jun_Max.Point, Jun_Max.Fdust_122, label='Max 06-28', marker='.', ms=8, ls='-', c='r', lw=2)
plt.plot(Jun_Min.Point, Jun_Min.Fdust_122, label='Min 06-29', marker='.', ms=8, ls='-', c='b', lw=2)
plt.plot(Jun_Mean.Point, Jun_Mean.Fdust_122, label='Mean 06-27', marker='.', ms=8, ls='-', c='g', lw=2)
xticks = ['[1]0:00', '[2]3:00', '[3]5:40', '[4]6:30', '[5]7:30', '[6]8:30\npeak',
          '[7]9:30', '[8]10:30', '[9]11:30', '[10]13:25', '[11]15:00', '[12]19:30', '[13]21:00', '[14]22:30']
plt.xticks(Jun_Max.Point, xticks, fontsize=13)
plt.grid(True, ls='--', c='lightgray')
plt.ylabel('터널 미세먼지\n')
plt.legend(fontsize=12)
plt.title('터널 미세먼지 - 부평삼거리 (6월)\n', fontsize=20)


######################################################################################################################## ON/OFF
File_List = glob.glob('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/4.data_Interpolated/*.csv')
for file in File_List:
    filename = file[-14:-4]
    filename = filename.replace('d-', '-')
    filename = filename[1:]

    if filename == '1-26-2017':
        JanFeb_Max = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/4.data_Interpolated/data_Combined-%s.csv' % filename, index_col=0)
    elif filename == '3-17-2017':
        Mar_Max = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/4.data_Interpolated/data_Combined-%s.csv' % filename, index_col=0)
    elif filename == '4-24-2017':
        Apr_Max = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/4.data_Interpolated/data_Combined-%s.csv' % filename, index_col=0)
    elif filename == '5-6-2017':
        May_Max = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/4.data_Interpolated/data_Combined-%s.csv' % filename, index_col=0)
    elif filename == '6-28-2017':
        Jun_Max = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/4.data_Interpolated/data_Combined-%s.csv' % filename, index_col=0)

    elif filename == '2-11-2017':
        JanFeb_Min = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/4.data_Interpolated/data_Combined-%s.csv' % filename, index_col=0)
    elif filename == '3-8-2017':
        Mar_Min = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/4.data_Interpolated/data_Combined-%s.csv' % filename, index_col=0)
    elif filename == '4-12-2017':
        Apr_Min = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/4.data_Interpolated/data_Combined-%s.csv' % filename, index_col=0)
    elif filename == '5-11-2017':
        May_Min = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/4.data_Interpolated/data_Combined-%s.csv' % filename, index_col=0)
    elif filename == '6-29-2017':
        Jun_Min = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/4.data_Interpolated/data_Combined-%s.csv' % filename, index_col=0)

    elif filename == '1-31-2017':
        Jan_Mean = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/4.data_Interpolated/data_Combined-%s.csv' % filename, index_col=0)
    elif filename == '2-12-2017':
        Feb_Mean = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/4.data_Interpolated/data_Combined-%s.csv' % filename, index_col=0)
    elif filename == '3-6-2017':
        Mar_Mean = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/4.data_Interpolated/data_Combined-%s.csv' % filename, index_col=0)
    elif filename == '4-9-2017':
        Apr_Mean = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/4.data_Interpolated/data_Combined-%s.csv' % filename, index_col=0)
    elif filename == '5-10-2017':
        May_Mean = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/4.data_Interpolated/data_Combined-%s.csv' % filename, index_col=0)
    elif filename == '6-27-2017':
        Jun_Mean = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/4.data_Interpolated/data_Combined-%s.csv' % filename, index_col=0)

###################################################### 1+2
        ax = plt.figure(2, figsize=(20, 24)).add_subplot(411)
        JanFeb_Max['Time'] = pd.to_datetime(JanFeb_Max['Time'], format='%H:%M:%S')
        plt.plot(JanFeb_Max['Time'], JanFeb_Max['Tas1_122'].values, label='본선급기1', linestyle='--', c='r', lw=2)
        plt.plot(JanFeb_Max['Time'], JanFeb_Max['Tas2_122'].values + 0.1, label='본선급기2', linestyle=':', c='r', lw=2)
        plt.plot(JanFeb_Max['Time'], JanFeb_Max['Tas3_122'].values + 0.2, label='본선급기3', linestyle='-', c='r', lw=2)
        plt.legend(fontsize=12)
        plt.grid(True, ls='--', c='lightgray')
        plt.title('터널 미세먼지 - 부평삼거리 (1,2월)\n', fontsize=20)

        ax = plt.figure(2, figsize=(20, 24)).add_subplot(412)
        JanFeb_Min['Time'] = pd.to_datetime(JanFeb_Min['Time'], format='%H:%M:%S')
        plt.plot(JanFeb_Min['Time'], JanFeb_Min['Tas1_122'].values, label='본선급기1', linestyle='--', c='b', lw=2)
        plt.plot(JanFeb_Min['Time'], JanFeb_Min['Tas2_122'].values + 0.1, label='본선급기2', linestyle=':', c='b', lw=2)
        plt.plot(JanFeb_Min['Time'], JanFeb_Min['Tas3_122'].values + 0.2, label='본선급기3', linestyle='-', c='b', lw=2)
        plt.legend(fontsize=12)
        plt.grid(True, ls='--', c='lightgray')

        ax = plt.figure(2, figsize=(20, 24)).add_subplot(413)
        Jan_Mean['Time'] = pd.to_datetime(Jan_Mean['Time'], format='%H:%M:%S')
        plt.plot(Jan_Mean['Time'], Jan_Mean['Tas1_122'].values, label='본선급기1', linestyle='--', c='g', lw=2)
        plt.plot(Jan_Mean['Time'], Jan_Mean['Tas2_122'].values + 0.1, label='본선급기2', linestyle=':', c='g', lw=2)
        plt.plot(Jan_Mean['Time'], Jan_Mean['Tas3_122'].values + 0.2, label='본선급기3', linestyle='-', c='g', lw=2)
        plt.legend(fontsize=12)
        plt.grid(True, ls='--', c='lightgray')

        ax = plt.figure(2, figsize=(20, 24)).add_subplot(414)
        Feb_Mean['Time'] = pd.to_datetime(Feb_Mean['Time'], format='%H:%M:%S')
        plt.plot(Feb_Mean['Time'], Feb_Mean['Tas1_122'].values, label='본선급기1', linestyle='--', c='m', lw=2)
        plt.plot(Feb_Mean['Time'], Feb_Mean['Tas2_122'].values + 0.1, label='본선급기2', linestyle=':', c='m', lw=2)
        plt.plot(Feb_Mean['Time'], Feb_Mean['Tas3_122'].values + 0.2, label='본선급기3', linestyle='-', c='m', lw=2)
        plt.legend(fontsize=12)
        plt.grid(True, ls='--', c='lightgray')

###################################################### 3
        ax = plt.figure(4, figsize=(20, 24)).add_subplot(311)
        Mar_Max['Time'] = pd.to_datetime(Mar_Max['Time'], format='%H:%M:%S')
        plt.plot(Mar_Max['Time'], Mar_Max['Tas1_122'].values, label='본선급기1', linestyle='--', c='r', lw=2)
        plt.plot(Mar_Max['Time'], Mar_Max['Tas2_122'].values + 0.1, label='본선급기2', linestyle=':', c='r', lw=2)
        plt.plot(Mar_Max['Time'], Mar_Max['Tas3_122'].values + 0.2, label='본선급기3', linestyle='-', c='r', lw=2)
        plt.legend(fontsize=12)
        plt.grid(True, ls='--', c='lightgray')
        plt.title('터널 미세먼지 - 부평삼거리 (3월)\n', fontsize=20)

        ax = plt.figure(4, figsize=(20, 24)).add_subplot(312)
        Mar_Min['Time'] = pd.to_datetime(Mar_Min['Time'], format='%H:%M:%S')
        plt.plot(Mar_Min['Time'], Mar_Min['Tas1_122'].values, label='본선급기1', linestyle='--', c='b', lw=2)
        plt.plot(Mar_Min['Time'], Mar_Min['Tas2_122'].values + 0.1, label='본선급기2', linestyle=':', c='b', lw=2)
        plt.plot(Mar_Min['Time'], Mar_Min['Tas3_122'].values + 0.2, label='본선급기3', linestyle='-', c='b', lw=2)
        plt.legend(fontsize=12)
        plt.grid(True, ls='--', c='lightgray')

        ax = plt.figure(4, figsize=(20, 24)).add_subplot(313)
        Mar_Mean['Time'] = pd.to_datetime(Mar_Mean['Time'], format='%H:%M:%S')
        plt.plot(Mar_Mean['Time'], Mar_Mean['Tas1_122'].values, label='본선급기1', linestyle='--', c='g', lw=2)
        plt.plot(Mar_Mean['Time'], Mar_Mean['Tas2_122'].values + 0.1, label='본선급기2', linestyle=':', c='g', lw=2)
        plt.plot(Mar_Mean['Time'], Mar_Mean['Tas3_122'].values + 0.2, label='본선급기3', linestyle='-', c='g', lw=2)
        plt.legend(fontsize=12)
        plt.grid(True, ls='--', c='lightgray')

###################################################### 4
        ax = plt.figure(6, figsize=(20, 24)).add_subplot(311)
        Apr_Max['Time'] = pd.to_datetime(Apr_Max['Time'], format='%H:%M:%S')
        plt.plot(Apr_Max['Time'], Apr_Max['Tas1_122'].values, label='본선급기1', linestyle='--', c='r', lw=2)
        plt.plot(Apr_Max['Time'], Apr_Max['Tas2_122'].values + 0.1, label='본선급기2', linestyle=':', c='r', lw=2)
        plt.plot(Apr_Max['Time'], Apr_Max['Tas3_122'].values + 0.2, label='본선급기3', linestyle='-', c='r', lw=2)
        plt.legend(fontsize=12)
        plt.grid(True, ls='--', c='lightgray')
        plt.title('터널 미세먼지 - 부평삼거리 (4월)\n', fontsize=20)

        ax = plt.figure(6, figsize=(20, 24)).add_subplot(312)
        Apr_Min['Time'] = pd.to_datetime(Apr_Min['Time'], format='%H:%M:%S')
        plt.plot(Apr_Min['Time'], Apr_Min['Tas1_122'].values, label='본선급기1', linestyle='--', c='b', lw=2)
        plt.plot(Apr_Min['Time'], Apr_Min['Tas2_122'].values + 0.1, label='본선급기2', linestyle=':', c='b', lw=2)
        plt.plot(Apr_Min['Time'], Apr_Min['Tas3_122'].values + 0.2, label='본선급기3', linestyle='-', c='b', lw=2)
        plt.legend(fontsize=12)
        plt.grid(True, ls='--', c='lightgray')

        ax = plt.figure(6, figsize=(20, 24)).add_subplot(313)
        Apr_Mean['Time'] = pd.to_datetime(Apr_Mean['Time'], format='%H:%M:%S')
        plt.plot(Apr_Mean['Time'], Apr_Mean['Tas1_122'].values, label='본선급기1', linestyle='--', c='g', lw=2)
        plt.plot(Apr_Mean['Time'], Apr_Mean['Tas2_122'].values + 0.1, label='본선급기2', linestyle=':', c='g', lw=2)
        plt.plot(Apr_Mean['Time'], Apr_Mean['Tas3_122'].values + 0.2, label='본선급기3', linestyle='-', c='g', lw=2)
        plt.legend(fontsize=12)
        plt.grid(True, ls='--', c='lightgray')

###################################################### 5
        ax = plt.figure(8, figsize=(20, 24)).add_subplot(311)
        May_Max['Time'] = pd.to_datetime(May_Max['Time'], format='%H:%M:%S')
        plt.plot(May_Max['Time'], May_Max['Tas1_122'].values, label='본선급기1', linestyle='--', c='r', lw=2)
        plt.plot(May_Max['Time'], May_Max['Tas2_122'].values + 0.1, label='본선급기2', linestyle=':', c='r', lw=2)
        plt.plot(May_Max['Time'], May_Max['Tas3_122'].values + 0.2, label='본선급기3', linestyle='-', c='r', lw=2)
        plt.legend(fontsize=12)
        plt.grid(True, ls='--', c='lightgray')
        plt.title('터널 미세먼지 - 부평삼거리 (5월)\n', fontsize=20)

        ax = plt.figure(8, figsize=(20, 24)).add_subplot(312)
        May_Min['Time'] = pd.to_datetime(May_Min['Time'], format='%H:%M:%S')
        plt.plot(May_Min['Time'], May_Min['Tas1_122'].values, label='본선급기1', linestyle='--', c='b', lw=2)
        plt.plot(May_Min['Time'], May_Min['Tas2_122'].values + 0.1, label='본선급기2', linestyle=':', c='b', lw=2)
        plt.plot(May_Min['Time'], May_Min['Tas3_122'].values + 0.2, label='본선급기3', linestyle='-', c='b', lw=2)
        plt.legend(fontsize=12)
        plt.grid(True, ls='--', c='lightgray')

        ax = plt.figure(8, figsize=(20, 24)).add_subplot(313)
        May_Mean['Time'] = pd.to_datetime(May_Mean['Time'], format='%H:%M:%S')
        plt.plot(May_Mean['Time'], May_Mean['Tas1_122'].values, label='본선급기1', linestyle='--', c='g', lw=2)
        plt.plot(May_Mean['Time'], May_Mean['Tas2_122'].values + 0.1, label='본선급기2', linestyle=':', c='g', lw=2)
        plt.plot(May_Mean['Time'], May_Mean['Tas3_122'].values + 0.2, label='본선급기3', linestyle='-', c='g', lw=2)
        plt.legend(fontsize=12)
        plt.grid(True, ls='--', c='lightgray')

###################################################### 6
        ax = plt.figure(10, figsize=(20, 24)).add_subplot(311)
        Jun_Max['Time'] = pd.to_datetime(Jun_Max['Time'], format='%H:%M:%S')
        plt.plot(Jun_Max['Time'], Jun_Max['Tas1_122'].values, label='본선급기1', linestyle='--', c='r', lw=2)
        plt.plot(Jun_Max['Time'], Jun_Max['Tas2_122'].values + 0.1, label='본선급기2', linestyle=':', c='r', lw=2)
        plt.plot(Jun_Max['Time'], Jun_Max['Tas3_122'].values + 0.2, label='본선급기3', linestyle='-', c='r', lw=2)
        plt.legend(fontsize=12)
        plt.grid(True, ls='--', c='lightgray')
        plt.title('터널 미세먼지 - 부평삼거리 (6월)\n', fontsize=20)

        ax = plt.figure(10, figsize=(20, 24)).add_subplot(312)
        Jun_Min['Time'] = pd.to_datetime(Jun_Min['Time'], format='%H:%M:%S')
        plt.plot(Jun_Min['Time'], Jun_Min['Tas1_122'].values, label='본선급기1', linestyle='--', c='b', lw=2)
        plt.plot(Jun_Min['Time'], Jun_Min['Tas2_122'].values + 0.1, label='본선급기2', linestyle=':', c='b', lw=2)
        plt.plot(Jun_Min['Time'], Jun_Min['Tas3_122'].values + 0.2, label='본선급기3', linestyle='-', c='b', lw=2)
        plt.legend(fontsize=12)
        plt.grid(True, ls='--', c='lightgray')

        ax = plt.figure(10, figsize=(20, 24)).add_subplot(313)
        Jun_Mean['Time'] = pd.to_datetime(Jun_Mean['Time'], format='%H:%M:%S')
        plt.plot(Jun_Mean['Time'], Jun_Mean['Tas1_122'].values, label='본선급기1', linestyle='--', c='g', lw=2)
        plt.plot(Jun_Mean['Time'], Jun_Mean['Tas2_122'].values + 0.1, label='본선급기2', linestyle=':', c='g', lw=2)
        plt.plot(Jun_Mean['Time'], Jun_Mean['Tas3_122'].values + 0.2, label='본선급기3', linestyle='-', c='g', lw=2)
        plt.legend(fontsize=12)
        plt.grid(True, ls='--', c='lightgray')

plt.show()