import glob
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

Report = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/7.Report_Final.csv')
count_row = Report.shape[0]
Report['Month'] = 0
Report['Month'] = Report['Date'].str[:1]

font_name = mpl.font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

# # 간석오거리
# Report = Report[['Month', 'Date', 'Time', 'Report_123']]
# print('123max\n', Report.loc[Report.groupby(['Month'])['Report_123'].idxmax()])
# print('123min\n', Report.loc[Report.groupby(['Month'])['Report_123'].idxmin()])
#
# print(Report.query('Month == "9" & 49 <= Report_123 <= 49.2'))
# print(Report.loc[Report['Report_123'] == 295.843704])
#
# # 간석오거리
# Report = Report[['Month', 'Date', 'Time', 'Report_123']]
# print('123max\n', Report.loc[Report.groupby(['Month'])['Report_123'].idxmax()])
# print('123min\n', Report.loc[Report.groupby(['Month'])['Report_123'].idxmin()])
#
# print(Report.query('Month == "9" & 39 <= Report_123 <= 40'))

####################################################################################################################### Number
##################################################### 1+2
# Max
JanFeb_x = Report[Report['Date'].str.contains('1-25-2017')]
JanFeb_x = JanFeb_x.sort_values(by='Point', ascending=True)
JanFeb_Max = JanFeb_x.groupby(JanFeb_x.Point).mean()
JanFeb_Max = JanFeb_Max['Report_123']
JanFeb_Max = JanFeb_Max.to_frame()
JanFeb_Max.reset_index(level='Point', inplace=True)
# Min
JanFeb_i = Report[Report['Date'].str.contains('2-2-2017')]
JanFeb_i = JanFeb_i.sort_values(by='Point', ascending=True)
JanFeb_Min = JanFeb_i.groupby(JanFeb_i.Point).mean()
JanFeb_Min = JanFeb_Min['Report_123']
JanFeb_Min = JanFeb_Min.to_frame()
JanFeb_Min.reset_index(level='Point', inplace=True)
# Mean
Jan_n = Report[Report['Date'].str.contains('1-26-2017')]
Jan_n = Jan_n.sort_values(by='Point', ascending=True)
Jan_Mean = Jan_n.groupby(Jan_n.Point).mean()
Jan_Mean = Jan_Mean['Report_123']
Jan_Mean = Jan_Mean.to_frame()
Jan_Mean.reset_index(level='Point', inplace=True)
# Mean
Feb_n = Report[Report['Date'].str.contains('2-2-2017')]
Feb_n = Feb_n.sort_values(by='Point', ascending=True)
Feb_Mean = Feb_n.groupby(Feb_n.Point).mean()
Feb_Mean = Feb_Mean['Report_123']
Feb_Mean = Feb_Mean.to_frame()
Feb_Mean.reset_index(level='Point', inplace=True)

plt.figure(1, figsize=(20, 24))
plt.plot(JanFeb_Max.Point, JanFeb_Max.Report_123, label='Max 01-25', marker='.', ms=8, ls='-', c='r', lw=2)
plt.plot(JanFeb_Min.Point, JanFeb_Min.Report_123, label='Min 02-02', marker='.', ms=8, ls='-', c='b', lw=2)
plt.plot(Jan_Mean.Point, Jan_Mean.Report_123, label='Mean 01-26', marker='.', ms=8, ls='-', c='g', lw=2)
plt.plot(Feb_Mean.Point, Feb_Mean.Report_123, label='Mean 02-02', marker='.', ms=8, ls='-', c='m', lw=2)
xticks = ['[1]0:00', '[2]3:00', '[3]5:40', '[4]6:30', '[5]7:30', '[6]8:30\npeak',
          '[7]9:30', '[8]10:30', '[9]11:30', '[10]13:25', '[11]15:00', '[12]19:30', '[13]21:00', '[14]22:30']
plt.xticks(JanFeb_Max.Point, xticks, fontsize=13)
plt.grid(True, ls='--', c='lightgray')
plt.ylabel('대합실 미세먼지\n')
plt.legend(fontsize=12)
plt.title('대합실 미세먼지 - 간석오거리 (1,2월)\n', fontsize=20)

###################################################### 3
# Max
Mar_x = Report[Report['Date'].str.contains('3-21-2017')]
Mar_x = Mar_x.sort_values(by='Point', ascending=True)
Mar_Max = Mar_x.groupby(Mar_x.Point).mean()
Mar_Max = Mar_Max['Report_123']
Mar_Max = Mar_Max.to_frame()
Mar_Max.reset_index(level='Point', inplace=True)
# Min
Mar_i = Report[Report['Date'].str.contains('3-23-2017')]
Mar_i = Mar_i.sort_values(by='Point', ascending=True)
Mar_Min = Mar_i.groupby(Mar_i.Point).mean()
Mar_Min = Mar_Min['Report_123']
Mar_Min = Mar_Min.to_frame()
Mar_Min.reset_index(level='Point', inplace=True)
# Mean
Mar_n = Report[Report['Date'].str.contains('3-12-2017')]
Mar_n = Mar_n.sort_values(by='Point', ascending=True)
Mar_Mean = Mar_n.groupby(Mar_n.Point).mean()
Mar_Mean = Mar_Mean['Report_123']
Mar_Mean = Mar_Mean.to_frame()
Mar_Mean.reset_index(level='Point', inplace=True)

plt.figure(3, figsize=(20, 24))
plt.plot(Mar_Max.Point, Mar_Max.Report_123, label='Max 03-21', marker='.', ms=8, ls='-', c='r', lw=2)
plt.plot(Mar_Min.Point, Mar_Min.Report_123, label='Min 03-23', marker='.', ms=8, ls='-', c='b', lw=2)
plt.plot(Mar_Mean.Point, Mar_Mean.Report_123, label='Mean 03-12', marker='.', ms=8, ls='-', c='g', lw=2)
xticks = ['[1]0:00', '[2]3:00', '[3]5:40', '[4]6:30', '[5]7:30', '[6]8:30\npeak',
          '[7]9:30', '[8]10:30', '[9]11:30', '[10]13:25', '[11]15:00', '[12]19:30', '[13]21:00', '[14]22:30']
plt.xticks(Mar_Max.Point, xticks, fontsize=13)
plt.grid(True, ls='--', c='lightgray')
plt.ylabel('대합실 미세먼지\n')
plt.legend(fontsize=12)
plt.title('대합실 미세먼지 - 간석오거리 (3월)\n', fontsize=20)

###################################################### 4
# Max
Apr_x = Report[Report['Date'].str.contains('4-22-2017')]
Apr_x = Apr_x.sort_values(by='Point', ascending=True)
Apr_Max = Apr_x.groupby(Apr_x.Point).mean()
Apr_Max = Apr_Max['Report_123']
Apr_Max = Apr_Max.to_frame()
Apr_Max.reset_index(level='Point', inplace=True)
# Min
Apr_i = Report[Report['Date'].str.contains('4-14-2017')]
Apr_i = Apr_i.sort_values(by='Point', ascending=True)
Apr_Min = Apr_i.groupby(Apr_i.Point).mean()
Apr_Min = Apr_Min['Report_123']
Apr_Min = Apr_Min.to_frame()
Apr_Min.reset_index(level='Point', inplace=True)
# Mean
Apr_n = Report[Report['Date'].str.contains('4-16-2017')]
Apr_n = Apr_n.sort_values(by='Point', ascending=True)
Apr_Mean = Apr_n.groupby(Apr_n.Point).mean()
Apr_Mean = Apr_Mean['Report_123']
Apr_Mean = Apr_Mean.to_frame()
Apr_Mean.reset_index(level='Point', inplace=True)

plt.figure(5, figsize=(20, 24))
plt.plot(Apr_Max.Point, Apr_Max.Report_123, label='Max 04-22', marker='.', ms=8, ls='-', c='r', lw=2)
plt.plot(Apr_Min.Point, Apr_Min.Report_123, label='Min 04-14', marker='.', ms=8, ls='-', c='b', lw=2)
plt.plot(Apr_Mean.Point, Apr_Mean.Report_123, label='Mean 04-16', marker='.', ms=8, ls='-', c='g', lw=2)
xticks = ['[1]0:00', '[2]3:00', '[3]5:40', '[4]6:30', '[5]7:30', '[6]8:30\npeak',
          '[7]9:30', '[8]10:30', '[9]11:30', '[10]13:25', '[11]15:00', '[12]19:30', '[13]21:00', '[14]22:30']
plt.xticks(Apr_Max.Point, xticks, fontsize=13)
plt.grid(True, ls='--', c='lightgray')
plt.ylabel('대합실 미세먼지\n')
plt.legend(fontsize=12)
plt.title('대합실 미세먼지 - 간석오거리 (4월)\n', fontsize=20)

###################################################### 5
# Max
May_x = Report[Report['Date'].str.contains('5-8-2017')]
May_x = May_x.sort_values(by='Point', ascending=True)
May_Max = May_x.groupby(May_x.Point).mean()
May_Max = May_Max['Report_123']
May_Max = May_Max.to_frame()
May_Max.reset_index(level='Point', inplace=True)
# Min
May_i = Report[Report['Date'].str.contains('5-31-2017')]
May_i = May_i.sort_values(by='Point', ascending=True)
May_Min = May_i.groupby(May_i.Point).mean()
May_Min = May_Min['Report_123']
May_Min = May_Min.to_frame()
May_Min.reset_index(level='Point', inplace=True)
# Mean
May_n = Report[Report['Date'].str.contains('5-13-2017')]
May_n = May_n.sort_values(by='Point', ascending=True)
May_Mean = May_n.groupby(May_n.Point).mean()
May_Mean = May_Mean['Report_123']
May_Mean = May_Mean.to_frame()
May_Mean.reset_index(level='Point', inplace=True)

plt.figure(7, figsize=(20, 24))
plt.plot(May_Max.Point, May_Max.Report_123, label='Max 05-08', marker='.', ms=8, ls='-', c='r', lw=2)
plt.plot(May_Min.Point, May_Min.Report_123, label='Min 05-31', marker='.', ms=8, ls='-', c='b', lw=2)
plt.plot(May_Mean.Point, May_Mean.Report_123, label='Mean 05-13', marker='.', ms=8, ls='-', c='g', lw=2)
xticks = ['[1]0:00', '[2]3:00', '[3]5:40', '[4]6:30', '[5]7:30', '[6]8:30\npeak',
          '[7]9:30', '[8]10:30', '[9]11:30', '[10]13:25', '[11]15:00', '[12]19:30', '[13]21:00', '[14]22:30']
plt.xticks(May_Max.Point, xticks, fontsize=13)
plt.grid(True, ls='--', c='lightgray')
plt.ylabel('대합실 미세먼지\n')
plt.legend(fontsize=12)
plt.title('대합실 미세먼지 - 간석오거리 (5월)\n', fontsize=20)

###################################################### 7
# Max
Jul_x = Report[Report['Date'].str.contains('7-12-2017')]
Jul_x = Jul_x.sort_values(by='Point', ascending=True)
Jul_Max = Jul_x.groupby(Jul_x.Point).mean()
Jul_Max = Jul_Max['Report_123']
Jul_Max = Jul_Max.to_frame()
Jul_Max.reset_index(level='Point', inplace=True)
# Min
Jul_i = Report[Report['Date'].str.contains('7-1-2017')]
Jul_i = Jul_i.sort_values(by='Point', ascending=True)
Jul_Min = Jul_i.groupby(Jul_i.Point).mean()
Jul_Min = Jul_Min['Report_123']
Jul_Min = Jul_Min.to_frame()
Jul_Min.reset_index(level='Point', inplace=True)
# Mean
Jul_n = Report[Report['Date'].str.contains('7-9-2017')]
Jul_n = Jul_n.sort_values(by='Point', ascending=True)
Jul_Mean = Jul_n.groupby(Jul_n.Point).mean()
Jul_Mean = Jul_Mean['Report_123']
Jul_Mean = Jul_Mean.to_frame()
Jul_Mean.reset_index(level='Point', inplace=True)

plt.figure(9, figsize=(20, 24))
plt.plot(Jul_Max.Point, Jul_Max.Report_123, label='Max 07-12', marker='.', ms=8, ls='-', c='r', lw=2)
plt.plot(Jul_Min.Point, Jul_Min.Report_123, label='Min 07-01', marker='.', ms=8, ls='-', c='b', lw=2)
plt.plot(Jul_Mean.Point, Jul_Mean.Report_123, label='Mean 07-09', marker='.', ms=8, ls='-', c='g', lw=2)
xticks = ['[1]0:00', '[2]3:00', '[3]5:40', '[4]6:30', '[5]7:30', '[6]8:30\npeak',
          '[7]9:30', '[8]10:30', '[9]11:30', '[10]13:25', '[11]15:00', '[12]19:30', '[13]21:00', '[14]22:30']
plt.xticks(Jul_Max.Point, xticks, fontsize=13)
plt.grid(True, ls='--', c='lightgray')
plt.ylabel('대합실 미세먼지\n')
plt.legend(fontsize=12)
plt.title('대합실 미세먼지 - 간석오거리 (7월)\n', fontsize=20)


######################################################################################################################## ON/OFF
File_List = glob.glob('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/4.data_Interpolated/*.csv')
for file in File_List:
    filename = file[-14:-4]
    filename = filename.replace('d-', '-')
    filename = filename[1:]

    if filename == '1-25-2017':
        JanFeb_Max = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/4.data_Interpolated/data_Combined-%s.csv' % filename, index_col=0)
    elif filename == '3-21-2017':
        Mar_Max = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/4.data_Interpolated/data_Combined-%s.csv' % filename, index_col=0)
    elif filename == '4-22-2017':
        Apr_Max = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/4.data_Interpolated/data_Combined-%s.csv' % filename, index_col=0)
    elif filename == '5-8-2017':
        May_Max = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/4.data_Interpolated/data_Combined-%s.csv' % filename, index_col=0)
    elif filename == '7-12-2017':
        Jul_Max = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/4.data_Interpolated/data_Combined-%s.csv' % filename, index_col=0)

    elif filename == '2-2-2017':
        JanFeb_Min = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/4.data_Interpolated/data_Combined-%s.csv' % filename, index_col=0)
    elif filename == '3-23-2017':
        Mar_Min = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/4.data_Interpolated/data_Combined-%s.csv' % filename, index_col=0)
    elif filename == '4-14-2017':
        Apr_Min = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/4.data_Interpolated/data_Combined-%s.csv' % filename, index_col=0)
    elif filename == '5-31-2017':
        May_Min = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/4.data_Interpolated/data_Combined-%s.csv' % filename, index_col=0)
    elif filename == '7-1-2017':
        Jul_Min = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/4.data_Interpolated/data_Combined-%s.csv' % filename, index_col=0)

    elif filename == '1-26-2017':
        Jan_Mean = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/4.data_Interpolated/data_Combined-%s.csv' % filename, index_col=0)
    elif filename == '2-2-2017':
        Feb_Mean = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/4.data_Interpolated/data_Combined-%s.csv' % filename, index_col=0)
    elif filename == '3-12-2017':
        Mar_Mean = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/4.data_Interpolated/data_Combined-%s.csv' % filename, index_col=0)
    elif filename == '4-16-2017':
        Apr_Mean = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/4.data_Interpolated/data_Combined-%s.csv' % filename, index_col=0)
    elif filename == '5-13-2017':
        May_Mean = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/4.data_Interpolated/data_Combined-%s.csv' % filename, index_col=0)
    elif filename == '7-9-2017':
        Jul_Mean = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/4.data_Interpolated/data_Combined-%s.csv' % filename, index_col=0)

###################################################### 1+2
        ax = plt.figure(2, figsize=(20, 24)).add_subplot(411)
        JanFeb_Max['Time'] = pd.to_datetime(JanFeb_Max['Time'], format='%H:%M:%S')
        plt.plot(JanFeb_Max['Time'], JanFeb_Max['Wr1_123'].values, label='대합실공조기1', linestyle='--', c='r', lw=2)
        plt.plot(JanFeb_Max['Time'], JanFeb_Max['Wr2_123'].values + 0.1, label='대합실공조기2', linestyle=':', c='r', lw=2)
        plt.plot(JanFeb_Max['Time'], JanFeb_Max['Wr3_123'].values + 0.2, label='대합실공조기3', linestyle='-', c='r', lw=2)
        plt.plot(JanFeb_Max['Time'], JanFeb_Max['Wr4_123'].values + 0.3, label='대합실공조기4', linestyle='-.', c='r', lw=2)
        plt.legend(fontsize=12)
        plt.grid(True, ls='--', c='lightgray')
        plt.title('대합실 미세먼지 - 간석오거리 (1,2월)\n', fontsize=20)

        ax = plt.figure(2, figsize=(20, 24)).add_subplot(412)
        JanFeb_Min['Time'] = pd.to_datetime(JanFeb_Min['Time'], format='%H:%M:%S')
        plt.plot(JanFeb_Min['Time'], JanFeb_Min['Wr1_123'].values, label='대합실공조기1', linestyle='--', c='b', lw=2)
        plt.plot(JanFeb_Min['Time'], JanFeb_Min['Wr2_123'].values + 0.1, label='대합실공조기2', linestyle=':', c='b', lw=2)
        plt.plot(JanFeb_Max['Time'], JanFeb_Max['Wr3_123'].values + 0.2, label='대합실공조기3', linestyle='-', c='b', lw=2)
        plt.plot(JanFeb_Max['Time'], JanFeb_Max['Wr4_123'].values + 0.3, label='대합실공조기4', linestyle='-.', c='b', lw=2)
        plt.legend(fontsize=12)
        plt.grid(True, ls='--', c='lightgray')

        ax = plt.figure(2, figsize=(20, 24)).add_subplot(413)
        Jan_Mean['Time'] = pd.to_datetime(Jan_Mean['Time'], format='%H:%M:%S')
        plt.plot(Jan_Mean['Time'], Jan_Mean['Wr1_123'].values, label='대합실공조기1', linestyle='--', c='g', lw=2)
        plt.plot(Jan_Mean['Time'], Jan_Mean['Wr2_123'].values + 0.1, label='대합실공조기2', linestyle=':', c='g', lw=2)
        plt.plot(Jan_Mean['Time'], Jan_Mean['Wr3_123'].values + 0.2, label='대합실공조기3', linestyle='-', c='g', lw=2)
        plt.plot(Jan_Mean['Time'], Jan_Mean['Wr4_123'].values + 0.3, label='대합실공조기4', linestyle='-.', c='g', lw=2)
        plt.legend(fontsize=12)
        plt.grid(True, ls='--', c='lightgray')

        ax = plt.figure(2, figsize=(20, 24)).add_subplot(414)
        Feb_Mean['Time'] = pd.to_datetime(Feb_Mean['Time'], format='%H:%M:%S')
        plt.plot(Feb_Mean['Time'], Feb_Mean['Wr1_123'].values, label='대합실공조기1', linestyle='--', c='m', lw=2)
        plt.plot(Feb_Mean['Time'], Feb_Mean['Wr2_123'].values + 0.1, label='대합실공조기2', linestyle=':', c='m', lw=2)
        plt.plot(Feb_Mean['Time'], Feb_Mean['Wr3_123'].values + 0.2, label='대합실공조기3', linestyle='-', c='m', lw=2)
        plt.plot(Feb_Mean['Time'], Feb_Mean['Wr4_123'].values + 0.3, label='대합실공조기4', linestyle='-.', c='m', lw=2)
        plt.legend(fontsize=12)
        plt.grid(True, ls='--', c='lightgray')

    ###################################################### 3
        ax = plt.figure(4, figsize=(20, 24)).add_subplot(311)
        Mar_Max['Time'] = pd.to_datetime(Mar_Max['Time'], format='%H:%M:%S')
        plt.plot(Mar_Max['Time'], Mar_Max['Wr1_123'].values, label='대합실공조기1', linestyle='--', c='r', lw=2)
        plt.plot(Mar_Max['Time'], Mar_Max['Wr2_123'].values + 0.1, label='대합실공조기2', linestyle=':', c='r', lw=2)
        plt.plot(Mar_Max['Time'], Mar_Max['Wr3_123'].values + 0.2, label='대합실공조기3', linestyle='-', c='r', lw=2)
        plt.plot(Mar_Max['Time'], Mar_Max['Wr4_123'].values + 0.3, label='대합실공조기4', linestyle='-.', c='r', lw=2)
        plt.legend(fontsize=12)
        plt.grid(True, ls='--', c='lightgray')
        plt.title('대합실 미세먼지 - 간석오거리 (3월)\n', fontsize=20)

        ax = plt.figure(4, figsize=(20, 24)).add_subplot(312)
        Mar_Min['Time'] = pd.to_datetime(Mar_Min['Time'], format='%H:%M:%S')
        plt.plot(Mar_Min['Time'], Mar_Min['Wr1_123'].values, label='대합실공조기1', linestyle='--', c='b', lw=2)
        plt.plot(Mar_Min['Time'], Mar_Min['Wr2_123'].values + 0.1, label='대합실공조기2', linestyle=':', c='b', lw=2)
        plt.plot(Mar_Min['Time'], Mar_Min['Wr3_123'].values + 0.2, label='대합실공조기3', linestyle='-', c='b', lw=2)
        plt.plot(Mar_Min['Time'], Mar_Min['Wr4_123'].values + 0.3, label='대합실공조기4', linestyle='-.', c='b', lw=2)
        plt.legend(fontsize=12)
        plt.grid(True, ls='--', c='lightgray')

        ax = plt.figure(4, figsize=(20, 24)).add_subplot(313)
        Mar_Mean['Time'] = pd.to_datetime(Mar_Mean['Time'], format='%H:%M:%S')
        plt.plot(Mar_Mean['Time'], Mar_Mean['Wr1_123'].values, label='대합실공조기1', linestyle='--', c='g', lw=2)
        plt.plot(Mar_Mean['Time'], Mar_Mean['Wr2_123'].values + 0.1, label='대합실공조기2', linestyle=':', c='g', lw=2)
        plt.plot(Mar_Mean['Time'], Mar_Mean['Wr3_123'].values + 0.2, label='대합실공조기3', linestyle='-', c='g', lw=2)
        plt.plot(Mar_Mean['Time'], Mar_Mean['Wr4_123'].values + 0.3, label='대합실공조기4', linestyle='-.', c='g', lw=2)
        plt.legend(fontsize=12)
        plt.grid(True, ls='--', c='lightgray')

    ###################################################### 4
        ax = plt.figure(6, figsize=(20, 24)).add_subplot(311)
        Apr_Max['Time'] = pd.to_datetime(Apr_Max['Time'], format='%H:%M:%S')
        plt.plot(Apr_Max['Time'], Apr_Max['Wr1_123'].values, label='대합실공조기1', linestyle='--', c='r', lw=2)
        plt.plot(Apr_Max['Time'], Apr_Max['Wr2_123'].values + 0.1, label='대합실공조기2', linestyle=':', c='r', lw=2)
        plt.plot(Apr_Max['Time'], Apr_Max['Wr3_123'].values + 0.2, label='대합실공조기3', linestyle='-', c='r', lw=2)
        plt.plot(Apr_Max['Time'], Apr_Max['Wr4_123'].values + 0.3, label='대합실공조기4', linestyle='-.', c='r', lw=2)
        plt.legend(fontsize=12)
        plt.grid(True, ls='--', c='lightgray')
        plt.title('대합실 미세먼지 - 간석오거리 (4월)\n', fontsize=20)

        ax = plt.figure(6, figsize=(20, 24)).add_subplot(312)
        Apr_Min['Time'] = pd.to_datetime(Apr_Min['Time'], format='%H:%M:%S')
        plt.plot(Apr_Min['Time'], Apr_Min['Wr1_123'].values, label='대합실공조기1', linestyle='--', c='b', lw=2)
        plt.plot(Apr_Min['Time'], Apr_Min['Wr2_123'].values + 0.1, label='대합실공조기2', linestyle=':', c='b', lw=2)
        plt.plot(Apr_Min['Time'], Apr_Min['Wr3_123'].values + 0.2, label='대합실공조기3', linestyle='-', c='b', lw=2)
        plt.plot(Apr_Min['Time'], Apr_Min['Wr4_123'].values + 0.3, label='대합실공조기4', linestyle='-.', c='b', lw=2)
        plt.legend(fontsize=12)
        plt.grid(True, ls='--', c='lightgray')

        ax = plt.figure(6, figsize=(20, 24)).add_subplot(313)
        Apr_Mean['Time'] = pd.to_datetime(Apr_Mean['Time'], format='%H:%M:%S')
        plt.plot(Apr_Mean['Time'], Apr_Mean['Wr1_123'].values, label='대합실공조기1', linestyle='--', c='g', lw=2)
        plt.plot(Apr_Mean['Time'], Apr_Mean['Wr2_123'].values + 0.1, label='대합실공조기2', linestyle=':', c='g', lw=2)
        plt.plot(Apr_Mean['Time'], Apr_Mean['Wr3_123'].values + 0.2, label='대합실공조기3', linestyle='-', c='g', lw=2)
        plt.plot(Apr_Mean['Time'], Apr_Mean['Wr4_123'].values + 0.3, label='대합실공조기4', linestyle='-.', c='g', lw=2)
        plt.legend(fontsize=12)
        plt.grid(True, ls='--', c='lightgray')

    ###################################################### 5
        ax = plt.figure(8, figsize=(20, 24)).add_subplot(311)
        May_Max['Time'] = pd.to_datetime(May_Max['Time'], format='%H:%M:%S')
        plt.plot(May_Max['Time'], May_Max['Wr1_123'].values, label='대합실공조기1', linestyle='--', c='r', lw=2)
        plt.plot(May_Max['Time'], May_Max['Wr2_123'].values + 0.1, label='대합실공조기2', linestyle=':', c='r', lw=2)
        plt.plot(May_Max['Time'], May_Max['Wr3_123'].values + 0.2, label='대합실공조기3', linestyle='-', c='r', lw=2)
        plt.plot(May_Max['Time'], May_Max['Wr4_123'].values + 0.3, label='대합실공조기4', linestyle='-.', c='r', lw=2)
        plt.legend(fontsize=12)
        plt.grid(True, ls='--', c='lightgray')
        plt.title('대합실 미세먼지 - 간석오거리 (5월)\n', fontsize=20)

        ax = plt.figure(8, figsize=(20, 24)).add_subplot(312)
        May_Min['Time'] = pd.to_datetime(May_Min['Time'], format='%H:%M:%S')
        plt.plot(May_Min['Time'], May_Min['Wr1_123'].values, label='대합실공조기1', linestyle='--', c='b', lw=2)
        plt.plot(May_Min['Time'], May_Min['Wr2_123'].values + 0.1, label='대합실공조기2', linestyle=':', c='b', lw=2)
        plt.plot(May_Min['Time'], May_Min['Wr3_123'].values + 0.2, label='대합실공조기3', linestyle='-', c='r', lw=2)
        plt.plot(May_Min['Time'], May_Min['Wr4_123'].values + 0.3, label='대합실공조기4', linestyle='-.', c='r', lw=2)
        plt.legend(fontsize=12)
        plt.grid(True, ls='--', c='lightgray')

        ax = plt.figure(8, figsize=(20, 24)).add_subplot(313)
        May_Mean['Time'] = pd.to_datetime(May_Mean['Time'], format='%H:%M:%S')
        plt.plot(May_Mean['Time'], May_Mean['Wr1_123'].values, label='대합실공조기1', linestyle='--', c='g', lw=2)
        plt.plot(May_Mean['Time'], May_Mean['Wr2_123'].values + 0.1, label='대합실공조기2', linestyle=':', c='g', lw=2)
        plt.plot(May_Mean['Time'], May_Mean['Wr3_123'].values + 0.2, label='대합실공조기3', linestyle='-', c='g', lw=2)
        plt.plot(May_Mean['Time'], May_Mean['Wr4_123'].values + 0.3, label='대합실공조기4', linestyle='-.', c='g', lw=2)
        plt.legend(fontsize=12)
        plt.grid(True, ls='--', c='lightgray')

    ###################################################### 7
        ax = plt.figure(10, figsize=(20, 24)).add_subplot(311)
        Jul_Max['Time'] = pd.to_datetime(Jul_Max['Time'], format='%H:%M:%S')
        plt.plot(Jul_Max['Time'], Jul_Max['Wr1_123'].values, label='대합실공조기1', linestyle='--', c='r', lw=2)
        plt.plot(Jul_Max['Time'], Jul_Max['Wr2_123'].values + 0.1, label='대합실공조기2', linestyle=':', c='r', lw=2)
        plt.plot(Jul_Max['Time'], Jul_Max['Wr3_123'].values + 0.2, label='대합실공조기3', linestyle='-', c='r', lw=2)
        plt.plot(Jul_Max['Time'], Jul_Max['Wr4_123'].values + 0.3, label='대합실공조기4', linestyle='-.', c='r', lw=2)
        plt.legend(fontsize=12)
        plt.grid(True, ls='--', c='lightgray')
        plt.title('대합실 미세먼지 - 간석오거리 (7월)\n', fontsize=20)

        ax = plt.figure(10, figsize=(20, 24)).add_subplot(312)
        Jul_Min['Time'] = pd.to_datetime(Jul_Min['Time'], format='%H:%M:%S')
        plt.plot(Jul_Min['Time'], Jul_Min['Wr1_123'].values, label='대합실공조기1', linestyle='--', c='b', lw=2)
        plt.plot(Jul_Min['Time'], Jul_Min['Wr2_123'].values + 0.1, label='대합실공조기2', linestyle=':', c='b', lw=2)
        plt.plot(Jul_Min['Time'], Jul_Min['Wr3_123'].values + 0.2, label='대합실공조기3', linestyle='-', c='b', lw=2)
        plt.plot(Jul_Min['Time'], Jul_Min['Wr4_123'].values + 0.3, label='대합실공조기4', linestyle='-.', c='b', lw=2)
        plt.legend(fontsize=12)
        plt.grid(True, ls='--', c='lightgray')

        ax = plt.figure(10, figsize=(20, 24)).add_subplot(313)
        Jul_Mean['Time'] = pd.to_datetime(Jul_Mean['Time'], format='%H:%M:%S')
        plt.plot(Jul_Mean['Time'], Jul_Mean['Wr1_123'].values, label='대합실공조기1', linestyle='--', c='g', lw=2)
        plt.plot(Jul_Mean['Time'], Jul_Mean['Wr2_123'].values + 0.1, label='대합실공조기2', linestyle=':', c='g', lw=2)
        plt.plot(Jul_Mean['Time'], Jul_Mean['Wr3_123'].values + 0.2, label='대합실공조기3', linestyle='-', c='g', lw=2)
        plt.plot(Jul_Mean['Time'], Jul_Mean['Wr4_123'].values + 0.3, label='대합실공조기4', linestyle='-.', c='g', lw=2)
        plt.legend(fontsize=12)
        plt.grid(True, ls='--', c='lightgray')


plt.show()