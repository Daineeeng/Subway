import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


SD = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/spring_dust.csv')
SD = SD.iloc[:, 1:]
SD = SD.sort_values(['Date','Point'], ascending=[True,True])
SD.rename(columns={'120_Report':'Report_120','121_Report':'Report_121','122_Report':'Report_122',
                   '123_Report':'Report_123','124_Report':'Report_124'}, inplace=True)

ST = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/spring_temp.csv')
ST = ST.iloc[:, 1:]
ST = ST.sort_values(['Date','Point'], ascending=[True,True])
ST.rename(columns={'120_Report':'Report_120','121_Report':'Report_121','122_Report':'Report_122',
                   '123_Report':'Report_123','124_Report':'Report_124'}, inplace=True)

SH = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/summer_heat.csv')
SH = SH.iloc[:, 1:]
SH = SH.sort_values(['Date','Point'], ascending=[True,True])
SH.rename(columns={'120_Report':'Report_120','121_Report':'Report_121','122_Report':'Report_122',
                   '123_Report':'Report_123','124_Report':'Report_124'}, inplace=True)

SR = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/summer_rain.csv')
SR = SR.iloc[:, 1:]
SR = SR.sort_values(['Date','Point'], ascending=[True,True])
SR.rename(columns={'120_Report':'Report_120','121_Report':'Report_121','122_Report':'Report_122',
                   '123_Report':'Report_123','124_Report':'Report_124'}, inplace=True)

AD = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/autumn_dust.csv')
AD = AD.iloc[:, 1:]
AD = AD.sort_values(['Date','Point'], ascending=[True,True])
AD.rename(columns={'120_Report':'Report_120','121_Report':'Report_121','122_Report':'Report_122',
                   '123_Report':'Report_123','124_Report':'Report_124'}, inplace=True)

AT = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/autumn_temp.csv')
AT = AT.iloc[:, 1:]
AT = AT.sort_values(['Date','Point'], ascending=[True,True])
AT.rename(columns={'120_Report':'Report_120','121_Report':'Report_121','122_Report':'Report_122',
                   '123_Report':'Report_123','124_Report':'Report_124'}, inplace=True)

WC = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/winter_cold.csv')
WC = WC.iloc[:, 1:]
WC = WC.sort_values(['Date','Point'], ascending=[True,True])
WC.rename(columns={'120_Report':'Report_120','121_Report':'Report_121','122_Report':'Report_122',
                   '123_Report':'Report_123','124_Report':'Report_124'}, inplace=True)

WS = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/winter_snow.csv')
WS = WS.iloc[:, 1:]
WS = WS.sort_values(['Date','Point'], ascending=[True,True])
WS.rename(columns={'120_Report':'Report_120','121_Report':'Report_121','122_Report':'Report_122',
                   '123_Report':'Report_123','124_Report':'Report_124'}, inplace=True)


# 부평삼거리
# Mean1 : Case8
#1
SD_mean = SD[['Point','Report_122']]
SD_mean = SD_mean.groupby(SD_mean.Point).mean()
SD_mean.reset_index(level='Point', inplace=True)
# 2
ST_mean = ST[['Point','Report_122']]
ST_mean = ST_mean.groupby(ST_mean.Point).mean()
ST_mean.reset_index(level='Point', inplace=True)
# 3
SH_mean = SH[['Point','Report_122']]
SH_mean = SH_mean.groupby(SH_mean.Point).mean()
SH_mean.reset_index(level='Point', inplace=True)
# 4
SR_mean = SR[['Point','Report_122']]
SR_mean = SR_mean.groupby(SR_mean.Point).mean()
SR_mean.reset_index(level='Point', inplace=True)
# 5
AD_mean = AD[['Point','Report_122']]
AD_mean = AD_mean.groupby(AD_mean.Point).mean()
AD_mean.reset_index(level='Point', inplace=True)
# 6
AT_mean = AT[['Point','Report_122']]
AT_mean = AT_mean.groupby(AT_mean.Point).mean()
AT_mean.reset_index(level='Point', inplace=True)
# 7
WC_mean = WC[['Point','Report_122']]
WC_mean = WC_mean.groupby(WC_mean.Point).mean()
WC_mean.reset_index(level='Point', inplace=True)
# 8
WS_mean = WS[['Point','Report_122']]
WS_mean = WS_mean.groupby(WS_mean.Point).mean()
WS_mean.reset_index(level='Point', inplace=True)


font_name = mpl.font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)



plt.figure(1, figsize=(20,24))
# 봄
# 환경보고서
plt.plot(SD_mean.Point, SD_mean.Report_122, marker='o', ms=10, ls='-', c='y', lw=2)
# 일교차
plt.plot(ST_mean.Point, ST_mean.Report_122, marker='o', ms=10, ls='-', c='green', lw=2)
# 여름
# 더위
plt.plot(SH_mean.Point, SH_mean.Report_122, marker='^', ms=10, ls='-', c='red', lw=2)
# 장마
plt.plot(SR_mean.Point, SR_mean.Report_122, marker='^', ms=10, ls='-', c='lightsalmon', lw=2)
# 가을
# 환경보고서
plt.plot(AD_mean.Point, AD_mean.Report_122, marker='s', ms=10, ls='-', c='mediumpurple', lw=2)
# 일교차
plt.plot(AT_mean.Point, AT_mean.Report_122, marker='s', ms=10, ls='-', c='orchid', lw=2)
# 겨울
# 한파
plt.plot(WC_mean.Point, WC_mean.Report_122, marker='*', ms=10, ls='-', c='blue', lw=2)
# 눈
plt.plot(WS_mean.Point, WS_mean.Report_122, marker='*', ms=10, ls='-', c='lightsteelblue', lw=2)
plt.legend(['봄 미세먼지', '봄 일교차',
            '여름 더위', '여름 장마',
            '가을 환경보고서', '가을 일교차',
            '겨울 한파','겨울 눈'])
plt.title('환경보고서 평균 - 부평삼거리 계절 특성별 Case8\n')
plt.xlabel('Time Point')
plt.ylabel('환경보고서 평균값\n')

# Mean2 : Season
# Spring
Spring = pd.concat([SD_mean,ST_mean])
Spring_mean = Spring.groupby(Spring.Point).mean()
Spring_mean.reset_index(level='Point', inplace=True)
# Summer
Summer = pd.concat([SH_mean,SR_mean])
Summer_mean = Summer.groupby(Summer.Point).mean()
Summer_mean.reset_index(level='Point', inplace=True)
# Autumn
Autumn = pd.concat([AD_mean,AT_mean])
Autumn_mean = Autumn.groupby(Autumn.Point).mean()
Autumn_mean.reset_index(level='Point', inplace=True)
# Winter
Winter = pd.concat([WC_mean,WS_mean])
Winter_mean = Winter.groupby(Winter.Point).mean()
Winter_mean.reset_index(level='Point', inplace=True)

plt.figure(2, figsize=(20,24))
# 봄
plt.plot(Spring_mean.Point, Spring_mean.Report_122, marker='o', ms=10, ls='-', c='green', lw=2)
# 여름
plt.plot(Summer_mean.Point, Summer_mean.Report_122, marker='^', ms=10, ls='-', c='red', lw=2)
# 가을
plt.plot(Autumn_mean.Point, Autumn_mean.Report_122, marker='s', ms=10, ls='-', c='orchid', lw=2)
# 겨울
plt.plot(Winter_mean.Point, Winter_mean.Report_122, marker='*', ms=10, ls='-', c='blue', lw=2)
plt.legend(['봄', '여름', '가을', '겨울'])
plt.title('환경보고서 평균 - 부평삼거리 계절 4\n')
plt.xlabel('Time Point')
plt.ylabel('환경보고서 평균값\n')
#
############################################################################################
# 간석오거리
# Mean1 : Case8
#1
SD_mean = SD.groupby(SD.Point).mean()
SD_mean = SD_mean['Report_123']
SD_mean = SD_mean.to_frame()
SD_mean.reset_index(level='Point', inplace=True)
# 2
ST_mean = ST.groupby(ST.Point).mean()
ST_mean = ST_mean['Report_123']
ST_mean = ST_mean.to_frame()
ST_mean.reset_index(level='Point', inplace=True)
# 3
SH_mean = SH.groupby(SH.Point).mean()
SH_mean = SH_mean['Report_123']
SH_mean = SH_mean.to_frame()
SH_mean.reset_index(level='Point', inplace=True)
# 4
SR_mean = SR.groupby(SR.Point).mean()
SR_mean = SR_mean['Report_123']
SR_mean = SR_mean.to_frame()
SR_mean.reset_index(level='Point', inplace=True)
# 5
AD_mean = AD.groupby(AD.Point).mean()
AD_mean = AD_mean['Report_123']
AD_mean = AD_mean.to_frame()
AD_mean.reset_index(level='Point', inplace=True)
# 6
AT_mean = AT.groupby(AT.Point).mean()
AT_mean = AT_mean['Report_123']
AT_mean = AT_mean.to_frame()
AT_mean.reset_index(level='Point', inplace=True)
# 7
WC_mean = WC.groupby(WC.Point).mean()
WC_mean = WC_mean['Report_123']
WC_mean = WC_mean.to_frame()
WC_mean.reset_index(level='Point', inplace=True)
# 8
WS_mean = WS.groupby(WS.Point).mean()
WS_mean = WS_mean['Report_123']
WS_mean = WS_mean.to_frame()
WS_mean.reset_index(level='Point', inplace=True)


font_name = mpl.font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)


plt.figure(3, figsize=(20,24))
# 봄
# 환경보고서
plt.plot(SD_mean.Point, SD_mean.Report_123, marker='o', ms=10, ls='-', c='y', lw=2)
# 일교차
plt.plot(ST_mean.Point, ST_mean.Report_123, marker='o', ms=10, ls='-', c='green', lw=2)
# 여름
# 더위
plt.plot(SH_mean.Point, SH_mean.Report_123, marker='^', ms=10, ls='-', c='red', lw=2)
# 장마
plt.plot(SR_mean.Point, SR_mean.Report_123, marker='^', ms=10, ls='-', c='lightsalmon', lw=2)
# 가을
# 환경보고서
plt.plot(AD_mean.Point, AD_mean.Report_123, marker='s', ms=10, ls='-', c='mediumpurple', lw=2)
# 일교차
plt.plot(AT_mean.Point, AT_mean.Report_123, marker='s', ms=10, ls='-', c='orchid', lw=2)
# 겨울
# 한파
plt.plot(WC_mean.Point, WC_mean.Report_123, marker='*', ms=10, ls='-', c='blue', lw=2)
# 눈
plt.plot(WS_mean.Point, WS_mean.Report_123, marker='*', ms=10, ls='-', c='lightsteelblue', lw=2)
plt.legend(['봄 미세먼지', '봄 일교차',
            '여름 더위', '여름 장마',
            '가을 환경보고서', '가을 일교차',
            '겨울 한파','겨울 눈'])
plt.title('환경보고서 평균 - 간석오거리 계절 특성별 Case8\n')
plt.xlabel('Time Point')
plt.ylabel('환경보고서 평균값\n')

# Mean2 : Season
# Spring
Spring = pd.concat([SD_mean,ST_mean])
Spring_mean = Spring.groupby(Spring.Point).mean()
Spring_mean.reset_index(level='Point', inplace=True)
# Summer
Summer = pd.concat([SH_mean,SR_mean])
Summer_mean = Summer.groupby(Summer.Point).mean()
Summer_mean.reset_index(level='Point', inplace=True)
# Autumn
Autumn = pd.concat([AD_mean,AT_mean])
Autumn_mean = Autumn.groupby(Autumn.Point).mean()
Autumn_mean.reset_index(level='Point', inplace=True)
# Winter
Winter = pd.concat([WC_mean,WS_mean])
Winter_mean = Winter.groupby(Winter.Point).mean()
Winter_mean.reset_index(level='Point', inplace=True)

plt.figure(4, figsize=(20,24))
# 봄
plt.plot(Spring_mean.Point, Spring_mean.Report_123, marker='o', ms=10, ls='-', c='green', lw=2)
# 여름
plt.plot(Summer_mean.Point, Summer_mean.Report_123, marker='^', ms=10, ls='-', c='red', lw=2)
# 가을
plt.plot(Autumn_mean.Point, Autumn_mean.Report_123, marker='s', ms=10, ls='-', c='orchid', lw=2)
# 겨울
plt.plot(Winter_mean.Point, Winter_mean.Report_123, marker='*', ms=10, ls='-', c='blue', lw=2)
plt.legend(['봄', '여름', '가을', '겨울'])
plt.title('환경보고서 평균 - 간석오거리 계절 4\n')
plt.xlabel('Time Point')
plt.ylabel('환경보고서 평균값\n')

plt.show()