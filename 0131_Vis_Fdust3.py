import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


SD = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/spring_dust.csv')
print(SD)
SD = SD.sort_values(['Date','Point'], ascending=[True,True])
SD.rename(columns={'122_Fdust':'Fdust'}, inplace=True)

ST = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/spring_temp.csv')
ST = ST.sort_values(['Date','Point'], ascending=[True,True])
ST.rename(columns={'122_Fdust':'Fdust'}, inplace=True)

SH = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/summer_heat.csv')
SH = SH.sort_values(['Date','Point'], ascending=[True,True])
SH.rename(columns={'122_Fdust':'Fdust'}, inplace=True)

SR = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/summer_rain.csv')
SR = SR.sort_values(['Date','Point'], ascending=[True,True])
SR.rename(columns={'122_Fdust':'Fdust'}, inplace=True)

AD = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/autumn_dust.csv')
AD = AD.sort_values(['Date','Point'], ascending=[True,True])
AD.rename(columns={'122_Fdust':'Fdust'}, inplace=True)

AT = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/autumn_temp.csv')
AT = AT.sort_values(['Date','Point'], ascending=[True,True])
AT.rename(columns={'122_Fdust':'Fdust'}, inplace=True)

WC = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/winter_cold.csv')
WC = WC.sort_values(['Date','Point'], ascending=[True,True])
WC.rename(columns={'122_Fdust':'Fdust'}, inplace=True)

WS = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/winter_snow.csv')
WS = WS.sort_values(['Date','Point'], ascending=[True,True])
WS.rename(columns={'122_Fdust':'Fdust'}, inplace=True)

# Mean1 : Case8
# 1
SD_mean = SD.groupby(SD.Point).mean()
SD_mean = SD_mean['Fdust']
SD_mean = SD_mean.to_frame()
SD_mean.reset_index(level='Point', inplace=True)
# 2
ST_mean = ST.groupby(ST.Point).mean()
ST_mean = ST_mean['Fdust']
ST_mean = ST_mean.to_frame()
ST_mean.reset_index(level='Point', inplace=True)
# 3
SH_mean = SH.groupby(SH.Point).mean()
SH_mean = SH_mean['Fdust']
SH_mean = SH_mean.to_frame()
SH_mean.reset_index(level='Point', inplace=True)
# 4
SR_mean = SR.groupby(SR.Point).mean()
SR_mean = SR_mean['Fdust']
SR_mean = SR_mean.to_frame()
SR_mean.reset_index(level='Point', inplace=True)
# 5
AD_mean = AD.groupby(AD.Point).mean()
AD_mean = AD_mean['Fdust']
AD_mean = AD_mean.to_frame()
AD_mean.reset_index(level='Point', inplace=True)
# 6
AT_mean = AT.groupby(AT.Point).mean()
AT_mean = AT_mean['Fdust']
AT_mean = AT_mean.to_frame()
AT_mean.reset_index(level='Point', inplace=True)
# 7
WC_mean = WC.groupby(WC.Point).mean()
WC_mean = WC_mean['Fdust']
WC_mean = WC_mean.to_frame()
WC_mean.reset_index(level='Point', inplace=True)
# 8
WS_mean = WS.groupby(WS.Point).mean()
WS_mean = WS_mean['Fdust']
WS_mean = WS_mean.to_frame()
WS_mean.reset_index(level='Point', inplace=True)


font_name = mpl.font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)


plt.figure(1, figsize=(20,24))
# 봄
# 미세먼지
plt.plot(SD_mean.Point, SD_mean.Fdust, marker='o', ms=10, ls='-', c='y', lw=2)
# 일교차
plt.plot(ST_mean.Point, ST_mean.Fdust, marker='o', ms=10, ls='-', c='green', lw=2)
# 여름
# 더위
plt.plot(SH_mean.Point, SH_mean.Fdust, marker='^', ms=10, ls='-', c='red', lw=2)
# 장마
plt.plot(SR_mean.Point, SR_mean.Fdust, marker='^', ms=10, ls='-', c='lightsalmon', lw=2)
# 가을
# 미세먼지
plt.plot(AD_mean.Point, AD_mean.Fdust, marker='s', ms=10, ls='-', c='mediumpurple', lw=2)
# 일교차
plt.plot(AT_mean.Point, AT_mean.Fdust, marker='s', ms=10, ls='-', c='orchid', lw=2)
# 겨울
# 한파
plt.plot(WC_mean.Point, WC_mean.Fdust, marker='*', ms=10, ls='-', c='blue', lw=2)
# 눈
plt.plot(WS_mean.Point, WS_mean.Fdust, marker='*', ms=10, ls='-', c='lightsteelblue', lw=2)
plt.legend(['봄 미세먼지', '봄 일교차',
            '여름 더위', '여름 장마',
            '가을 미세먼지', '가을 일교차',
            '겨울 한파','겨울 눈'])
plt.title('미세먼지 평균 - 계절 특성별 Case8\n', fontsize=20)
plt.xlabel('Time Point')
plt.ylabel('미세먼지 평균값\n')


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
plt.plot(Spring_mean.Point, Spring_mean.Fdust, marker='o', ms=10, ls='-', c='green', lw=2)
# 여름
plt.plot(Summer_mean.Point, Summer_mean.Fdust, marker='^', ms=10, ls='-', c='red', lw=2)
# 가을
plt.plot(Autumn_mean.Point, Autumn_mean.Fdust, marker='s', ms=10, ls='-', c='orchid', lw=2)
# 겨울
plt.plot(Winter_mean.Point, Winter_mean.Fdust, marker='*', ms=10, ls='-', c='blue', lw=2)
plt.legend(['봄', '여름', '가을', '겨울'])
plt.title('미세먼지 평균 - 계절 4\n', fontsize=20)
plt.xlabel('Time Point')
plt.ylabel('미세먼지 평균값\n')

plt.show()