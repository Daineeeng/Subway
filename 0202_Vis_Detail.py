import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

Fdust = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/7.Fdust_Final.csv')
Fdust = Fdust[Fdust.Point!=0]
Fdust.rename(columns={'122_Fdust':'Fdust'}, inplace=True)

# 1+2
Jan = Fdust[Fdust['Date'].str.contains('2017-01')]
Feb = Fdust[Fdust['Date'].str.contains('2017-02')]
Feb = pd.concat([Jan,Feb])
Feb_mean = Feb.groupby(Feb.Point).mean()
Feb_mean = Feb_mean['Fdust']
Feb_mean = Feb_mean.to_frame()
Feb_mean.reset_index(level='Point', inplace=True)
# 3
Mar = Fdust[Fdust['Date'].str.contains('2017-03')]
Mar_mean = Mar.groupby(Mar.Point).mean()
Mar_mean = Mar_mean['Fdust']
Mar_mean = Mar_mean.to_frame()
Mar_mean.reset_index(level='Point', inplace=True)
# 4
Apr = Fdust[Fdust['Date'].str.contains('2017-04')]
Apr_mean = Apr.groupby(Apr.Point).mean()
Apr_mean = Apr_mean['Fdust']
Apr_mean = Apr_mean.to_frame()
Apr_mean.reset_index(level='Point', inplace=True)
# 5
May = Fdust[Fdust['Date'].str.contains('2017-05')]
May_mean = May.groupby(May.Point).mean()
May_mean = May_mean['Fdust']
May_mean = May_mean.to_frame()
May_mean.reset_index(level='Point', inplace=True)
# 6
Jun = Fdust[Fdust['Date'].str.contains('2017-06')]
Jun_mean = Jun.groupby(Jun.Point).mean()
Jun_mean = Jun_mean['Fdust']
Jun_mean = Jun_mean.to_frame()
Jun_mean.reset_index(level='Point', inplace=True)
# 7
Jul = Fdust[Fdust['Date'].str.contains('2017-07')]
Jul_mean = Jul.groupby(Jul.Point).mean()
Jul_mean = Jul_mean['Fdust']
Jul_mean = Jul_mean.to_frame()
Jul_mean.reset_index(level='Point', inplace=True)
# 8
Aug = Fdust[Fdust['Date'].str.contains('2017-08')]
Aug_mean = Aug.groupby(Aug.Point).mean()
Aug_mean = Aug_mean['Fdust']
Aug_mean = Aug_mean.to_frame()
Aug_mean.reset_index(level='Point', inplace=True)
# 9
Sep = Fdust[Fdust['Date'].str.contains('2017-09')]
Sep_mean = Sep.groupby(Sep.Point).mean()
Sep_mean = Sep_mean['Fdust']
Sep_mean = Sep_mean.to_frame()
Sep_mean.reset_index(level='Point', inplace=True)


font_name = mpl.font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)


plt.figure(1, figsize=(20,24))
xticks = ['[1]0:00', '[2]3:00', '[3]5:40', '[4]6:35', '[5]7:20', '[6]8:30', '[7]13:25', '[8]15:00', '[9]19:30', '[10]21:00', '[11]22:30']
plt.xticks(Feb_mean.Point, xticks)
# 1+2
plt.plot(Feb_mean.Point, Feb_mean.Fdust, marker='.', ms=8, ls='-', c='r', lw=2)
# # 3
plt.plot(Mar_mean.Point, Mar_mean.Fdust, marker='.', ms=8, ls='-', c='darkorange', lw=2)
# 4
plt.plot(Apr_mean.Point, Apr_mean.Fdust, marker='.', ms=8, ls='-', c='y', lw=2)
# 8
plt.plot(May_mean.Point, May_mean.Fdust, marker='.', ms=8, ls='-', c='g', lw=2)
# 6
plt.plot(Jun_mean.Point, Jun_mean.Fdust, marker='.', ms=8, ls='-', c='c', lw=2)
# 7
plt.plot(Jul_mean.Point, Jul_mean.Fdust, marker='.', ms=8, ls='-', c='b', lw=2)
# 8
plt.plot(Aug_mean.Point, Aug_mean.Fdust, marker='.', ms=8, ls='-', c='m', lw=2)
# 9
plt.plot(Sep_mean.Point, Sep_mean.Fdust, marker='.', ms=8, ls='-', c='k', lw=2)
plt.ylabel('미세먼지 평균값\n')
plt.xlabel('\nTime Point')
plt.legend(['1월+2월','3월','4월','5월','6월','7월','8월','9월'])
plt.title('미세먼지 - 월별 평균값 (부평삼거리)\n', fontsize=20)

# ######################################################################################

Report = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/7.Report_Final.csv')
Report = Report[Report.Point!=0]
Report.rename(columns={'122_Report':'Report'}, inplace=True)

# 1+2
Jan = Report[Report['Date'].str.contains('2017-01')]
Feb = Report[Report['Date'].str.contains('2017-02')]
Feb = pd.concat([Jan,Feb])
Feb_mean = Feb.groupby(Feb.Point).mean()
Feb_mean = Feb_mean['Report']
Feb_mean = Feb_mean.to_frame()
Feb_mean.reset_index(level='Point', inplace=True)
# 3
Mar = Report[Report['Date'].str.contains('2017-03')]
Mar_mean = Mar.groupby(Mar.Point).mean()
Mar_mean = Mar_mean['Report']
Mar_mean = Mar_mean.to_frame()
Mar_mean.reset_index(level='Point', inplace=True)
# 4
Apr = Report[Report['Date'].str.contains('2017-04')]
Apr_mean = Apr.groupby(Apr.Point).mean()
Apr_mean = Apr_mean['Report']
Apr_mean = Apr_mean.to_frame()
Apr_mean.reset_index(level='Point', inplace=True)
# 5
May = Report[Report['Date'].str.contains('2017-05')]
May_mean = May.groupby(May.Point).mean()
May_mean = May_mean['Report']
May_mean = May_mean.to_frame()
May_mean.reset_index(level='Point', inplace=True)
# 6
Jun = Report[Report['Date'].str.contains('2017-06')]
Jun_mean = Jun.groupby(Jun.Point).mean()
Jun_mean = Jun_mean['Report']
Jun_mean = Jun_mean.to_frame()
Jun_mean.reset_index(level='Point', inplace=True)
# 7
Jul = Report[Report['Date'].str.contains('2017-07')]
Jul_mean = Jul.groupby(Jul.Point).mean()
Jul_mean = Jul_mean['Report']
Jul_mean = Jul_mean.to_frame()
Jul_mean.reset_index(level='Point', inplace=True)
# 8
Aug = Report[Report['Date'].str.contains('2017-08')]
Aug_mean = Aug.groupby(Aug.Point).mean()
Aug_mean = Aug_mean['Report']
Aug_mean = Aug_mean.to_frame()
Aug_mean.reset_index(level='Point', inplace=True)
# 9
Sep = Report[Report['Date'].str.contains('2017-09')]
Sep_mean = Sep.groupby(Sep.Point).mean()
Sep_mean = Sep_mean['Report']
Sep_mean = Sep_mean.to_frame()
Sep_mean.reset_index(level='Point', inplace=True)


font_name = mpl.font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)


plt.figure(2, figsize=(20,24))
xticks = ['[1]0:00', '[2]3:00', '[3]5:40', '[4]6:35', '[5]7:20', '[6]8:30', '[7]13:25', '[8]15:00', '[9]19:30', '[10]21:00', '[11]22:30']
plt.xticks(Feb_mean.Point, xticks)
# 1+2
plt.plot(Feb_mean.Point, Feb_mean.Report, marker='.', ms=8, ls='-', c='r', lw=2)
# # 3
plt.plot(Mar_mean.Point, Mar_mean.Report, marker='.', ms=8, ls='-', c='darkorange', lw=2)
# 4
plt.plot(Apr_mean.Point, Apr_mean.Report, marker='.', ms=8, ls='-', c='y', lw=2)
# 8
plt.plot(May_mean.Point, May_mean.Report, marker='.', ms=8, ls='-', c='g', lw=2)
# 6
plt.plot(Jun_mean.Point, Jun_mean.Report, marker='.', ms=8, ls='-', c='c', lw=2)
# 7
plt.plot(Jul_mean.Point, Jul_mean.Report, marker='.', ms=8, ls='-', c='b', lw=2)
# 8
plt.plot(Aug_mean.Point, Aug_mean.Report, marker='.', ms=8, ls='-', c='m', lw=2)
# 9
plt.plot(Sep_mean.Point, Sep_mean.Report, marker='.', ms=8, ls='-', c='k', lw=2)
plt.ylabel('환경보고서 평균값\n')
plt.xlabel('\nTime Point')
plt.legend(['1월+2월','3월','4월','5월','6월','7월','8월','9월'])
plt.title('환경보고서 - 월별 평균값 (부평삼거리)\n', fontsize=20)

# ######################################################################################

Report = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/7.Report_Final.csv')
Report = Report[Report.Point!=0]
Report.rename(columns={'123_Report':'Report'}, inplace=True)

# 1+2
Jan = Report[Report['Date'].str.contains('2017-01')]
Feb = Report[Report['Date'].str.contains('2017-02')]
Feb = pd.concat([Jan,Feb])
Feb_mean = Feb.groupby(Feb.Point).mean()
Feb_mean = Feb_mean['Report']
Feb_mean = Feb_mean.to_frame()
Feb_mean.reset_index(level='Point', inplace=True)
# 3
Mar = Report[Report['Date'].str.contains('2017-03')]
Mar_mean = Mar.groupby(Mar.Point).mean()
Mar_mean = Mar_mean['Report']
Mar_mean = Mar_mean.to_frame()
Mar_mean.reset_index(level='Point', inplace=True)
# 4
Apr = Report[Report['Date'].str.contains('2017-04')]
Apr_mean = Apr.groupby(Apr.Point).mean()
Apr_mean = Apr_mean['Report']
Apr_mean = Apr_mean.to_frame()
Apr_mean.reset_index(level='Point', inplace=True)
# 5
May = Report[Report['Date'].str.contains('2017-05')]
May_mean = May.groupby(May.Point).mean()
May_mean = May_mean['Report']
May_mean = May_mean.to_frame()
May_mean.reset_index(level='Point', inplace=True)
# 6
Jun = Report[Report['Date'].str.contains('2017-06')]
Jun_mean = Jun.groupby(Jun.Point).mean()
Jun_mean = Jun_mean['Report']
Jun_mean = Jun_mean.to_frame()
Jun_mean.reset_index(level='Point', inplace=True)
# 7
Jul = Report[Report['Date'].str.contains('2017-07')]
Jul_mean = Jul.groupby(Jul.Point).mean()
Jul_mean = Jul_mean['Report']
Jul_mean = Jul_mean.to_frame()
Jul_mean.reset_index(level='Point', inplace=True)
# 8
Aug = Report[Report['Date'].str.contains('2017-08')]
Aug_mean = Aug.groupby(Aug.Point).mean()
Aug_mean = Aug_mean['Report']
Aug_mean = Aug_mean.to_frame()
Aug_mean.reset_index(level='Point', inplace=True)
# 9
Sep = Report[Report['Date'].str.contains('2017-09')]
Sep_mean = Sep.groupby(Sep.Point).mean()
Sep_mean = Sep_mean['Report']
Sep_mean = Sep_mean.to_frame()
Sep_mean.reset_index(level='Point', inplace=True)


font_name = mpl.font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)


plt.figure(3, figsize=(20,24))
xticks = ['[1]0:00', '[2]3:00', '[3]5:40', '[4]6:35', '[5]7:20', '[6]8:30', '[7]13:25', '[8]15:00', '[9]19:30', '[10]21:00', '[11]22:30']
plt.xticks(Feb_mean.Point, xticks)
# 1+2
plt.plot(Feb_mean.Point, Feb_mean.Report, marker='.', ms=8, ls='-', c='r', lw=2)
# # 3
plt.plot(Mar_mean.Point, Mar_mean.Report, marker='.', ms=8, ls='-', c='darkorange', lw=2)
# 4
plt.plot(Apr_mean.Point, Apr_mean.Report, marker='.', ms=8, ls='-', c='y', lw=2)
# 8
plt.plot(May_mean.Point, May_mean.Report, marker='.', ms=8, ls='-', c='g', lw=2)
# 6
plt.plot(Jun_mean.Point, Jun_mean.Report, marker='.', ms=8, ls='-', c='c', lw=2)
# 7
plt.plot(Jul_mean.Point, Jul_mean.Report, marker='.', ms=8, ls='-', c='b', lw=2)
# 8
plt.plot(Aug_mean.Point, Aug_mean.Report, marker='.', ms=8, ls='-', c='m', lw=2)
# 9
plt.plot(Sep_mean.Point, Sep_mean.Report, marker='.', ms=8, ls='-', c='k', lw=2)

plt.ylabel('환경보고서 평균값\n')
plt.xlabel('\nTime Point')
plt.legend(['1월+2월','3월','4월','5월','6월','7월','8월','9월'])
plt.title('환경보고서 - 월별 평균값 (간석오거리)\n', fontsize=20)

# ######################################################################################

Report = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/7.Report_Final.csv')
Report = Report[Report.Point!=0]
Report.rename(columns={'120_Report':'Report'}, inplace=True)

# 1+2
Jan = Report[Report['Date'].str.contains('2017-01')]
Feb = Report[Report['Date'].str.contains('2017-02')]
Feb = pd.concat([Jan,Feb])
Feb_mean = Feb.groupby(Feb.Point).mean()
Feb_mean = Feb_mean['Report']
Feb_mean = Feb_mean.to_frame()
Feb_mean.reset_index(level='Point', inplace=True)
# 3
Mar = Report[Report['Date'].str.contains('2017-03')]
Mar_mean = Mar.groupby(Mar.Point).mean()
Mar_mean = Mar_mean['Report']
Mar_mean = Mar_mean.to_frame()
Mar_mean.reset_index(level='Point', inplace=True)
# 4
Apr = Report[Report['Date'].str.contains('2017-04')]
Apr_mean = Apr.groupby(Apr.Point).mean()
Apr_mean = Apr_mean['Report']
Apr_mean = Apr_mean.to_frame()
Apr_mean.reset_index(level='Point', inplace=True)
# 5
May = Report[Report['Date'].str.contains('2017-05')]
May_mean = May.groupby(May.Point).mean()
May_mean = May_mean['Report']
May_mean = May_mean.to_frame()
May_mean.reset_index(level='Point', inplace=True)
# 6
Jun = Report[Report['Date'].str.contains('2017-06')]
Jun_mean = Jun.groupby(Jun.Point).mean()
Jun_mean = Jun_mean['Report']
Jun_mean = Jun_mean.to_frame()
Jun_mean.reset_index(level='Point', inplace=True)
# 7
Jul = Report[Report['Date'].str.contains('2017-07')]
Jul_mean = Jul.groupby(Jul.Point).mean()
Jul_mean = Jul_mean['Report']
Jul_mean = Jul_mean.to_frame()
Jul_mean.reset_index(level='Point', inplace=True)
# 8
Aug = Report[Report['Date'].str.contains('2017-08')]
Aug_mean = Aug.groupby(Aug.Point).mean()
Aug_mean = Aug_mean['Report']
Aug_mean = Aug_mean.to_frame()
Aug_mean.reset_index(level='Point', inplace=True)
# 9
Sep = Report[Report['Date'].str.contains('2017-09')]
Sep_mean = Sep.groupby(Sep.Point).mean()
Sep_mean = Sep_mean['Report']
Sep_mean = Sep_mean.to_frame()
Sep_mean.reset_index(level='Point', inplace=True)


font_name = mpl.font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)


plt.figure(4, figsize=(20,24))
xticks = ['[1]0:00', '[2]3:00', '[3]5:40', '[4]6:35', '[5]7:20', '[6]8:30', '[7]13:25', '[8]15:00', '[9]19:30', '[10]21:00', '[11]22:30']
plt.xticks(Feb_mean.Point, xticks)
# 1+2
plt.plot(Feb_mean.Point, Feb_mean.Report, marker='.', ms=8, ls='-', c='r', lw=2)
# # 3
plt.plot(Mar_mean.Point, Mar_mean.Report, marker='.', ms=8, ls='-', c='darkorange', lw=2)
# 4
plt.plot(Apr_mean.Point, Apr_mean.Report, marker='.', ms=8, ls='-', c='y', lw=2)
# 8
plt.plot(May_mean.Point, May_mean.Report, marker='.', ms=8, ls='-', c='g', lw=2)
# 6
plt.plot(Jun_mean.Point, Jun_mean.Report, marker='.', ms=8, ls='-', c='c', lw=2)
# 7
plt.plot(Jul_mean.Point, Jul_mean.Report, marker='.', ms=8, ls='-', c='b', lw=2)
# 8
plt.plot(Aug_mean.Point, Aug_mean.Report, marker='.', ms=8, ls='-', c='m', lw=2)
# 9
plt.plot(Sep_mean.Point, Sep_mean.Report, marker='.', ms=8, ls='-', c='k', lw=2)

plt.ylabel('환경보고서 평균값\n')
plt.xlabel('\nTime Point')
plt.legend(['1월+2월','3월','4월','5월','6월','7월','8월','9월'])
plt.title('환경보고서 - 월별 평균값 (부평)\n', fontsize=20)

plt.show()