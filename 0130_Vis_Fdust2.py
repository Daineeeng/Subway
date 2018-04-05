import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


SD = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/spring_dust.csv')
SD = SD.iloc[:, 1:]
SD = SD.sort_values(['Date','Point'], ascending=[True,True])
SD.rename(columns={'122_Fdust':'Fdust'}, inplace=True)

ST = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/spring_temp.csv')
ST = ST.iloc[:, 1:]
ST = ST.sort_values(['Date','Point'], ascending=[True,True])
ST.rename(columns={'122_Fdust':'Fdust'}, inplace=True)

SH = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/summer_heat.csv')
SH = SH.iloc[:, 1:]
SH = SH.sort_values(['Date','Point'], ascending=[True,True])
SH.rename(columns={'122_Fdust':'Fdust'}, inplace=True)

SR = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/summer_rain.csv')
SR = SR.iloc[:, 1:]
SR = SR.sort_values(['Date','Point'], ascending=[True,True])
SR.rename(columns={'122_Fdust':'Fdust'}, inplace=True)

AD = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/autumn_dust.csv')
AD = AD.iloc[:, 1:]
AD = AD.sort_values(['Date','Point'], ascending=[True,True])
AD.rename(columns={'122_Fdust':'Fdust'}, inplace=True)

AT = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/autumn_temp.csv')
AT = AT.iloc[:, 1:]
AT = AT.sort_values(['Date','Point'], ascending=[True,True])
AT.rename(columns={'122_Fdust':'Fdust'}, inplace=True)

WC = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/winter_cold.csv')
WC = WC.iloc[:, 1:]
WC = WC.sort_values(['Date','Point'], ascending=[True,True])
WC.rename(columns={'122_Fdust':'Fdust'}, inplace=True)

WS = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/winter_snow.csv')
WS = WS.iloc[:, 1:]
WS = WS.sort_values(['Date','Point'], ascending=[True,True])
WS.rename(columns={'122_Fdust':'Fdust'}, inplace=True)


SD1 = SD[SD.Date=='2017-05-05']
SD1 = SD1[['Point','Date','Fdust']]
SD2 = SD[SD.Date=='2017-05-06']
SD2 = SD2[['Point','Date','Fdust']]
SD3 = SD[SD.Date=='2017-05-07']
SD3 = SD3[['Point','Date','Fdust']]

ST1 = ST[ST.Date=='2017-05-02']
ST1 = ST1[['Point','Date','Fdust']]
ST2 = ST[ST.Date=='2017-05-03']
ST2 = ST2[['Point','Date','Fdust']]
ST3 = ST[ST.Date=='2017-05-04']
ST3 = ST3[['Point','Date','Fdust']]

SH1 = SH[SH.Date=='2017-08-04']
SH1 = SH1[['Point','Date','Fdust']]
SH2 = SH[SH.Date=='2017-08-05']
SH2 = SH2[['Point','Date','Fdust']]
SH3 = SH[SH.Date=='2017-08-06']
SH3 = SH3[['Point','Date','Fdust']]

SR1 = SR[SR.Date=='2017-07-01']
SR1 = SR1[['Point','Date','Fdust']]
SR2 = SR[SR.Date=='2017-07-02']
SR2 = SR2[['Point','Date','Fdust']]
SR3 = SR[SR.Date=='2017-07-03']
SR3 = SR3[['Point','Date','Fdust']]

AD1 = AD[AD.Date=='2017-09-16']
AD1 = AD1[['Point','Date','Fdust']]
AD2 = AD[AD.Date=='2017-09-17']
AD2 = AD2[['Point','Date','Fdust']]
AD3 = AD[AD.Date=='2017-09-18']
AD3 = AD3[['Point','Date','Fdust']]

AT1 = AT[AT.Date=='2017-09-13']
AT1 = AT1[['Point','Date','Fdust']]
AT2 = AT[AT.Date=='2017-09-14']
AT2 = AT2[['Point','Date','Fdust']]
AT3 = AT[AT.Date=='2017-09-15']
AT3 = AT3[['Point','Date','Fdust']]

WC1 = WC[WC.Date=='2017-01-26']
WC1 = WC1[['Point','Date','Fdust']]
WC2 = WC[WC.Date=='2017-01-27']
WC2 = WC2[['Point','Date','Fdust']]
WC3 = WC[WC.Date=='2017-01-28']
WC3 = WC3[['Point','Date','Fdust']]

WS1 = WS[WS.Date=='2017-01-29']
WS1 = WS1[['Point','Date','Fdust']]
WS2 = WS[WS.Date=='2017-01-30']
WS2 = WS2[['Point','Date','Fdust']]
WS3 = WS[WS.Date=='2017-01-31']
WS3 = WS3[['Point','Date','Fdust']]


font_name = mpl.font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)
plt.figure(figsize=(23,60))


# 봄
# 미세먼지
plt.plot(SD1.Point, SD1.Fdust, marker='v', ls=':', c='y', lw=2)
plt.plot(SD2.Point, SD2.Fdust, marker='v', ls='-', c='y', lw=2)
plt.plot(SD3.Point, SD3.Fdust, marker='v', ls='--', c='y', lw=2)
# 일교차
plt.plot(ST1.Point, ST1.Fdust, marker='^', ls=':', c='green', lw=2)
plt.plot(ST2.Point, ST2.Fdust, marker='^', ls='-', c='green', lw=2)
plt.plot(ST3.Point, ST3.Fdust, marker='^', ls='--', c='green', lw=2)

# 여름
# 더위
plt.plot(SH1.Point, SH1.Fdust, marker='v', ls=':', c='red', lw=2)
plt.plot(SH2.Point, SH2.Fdust, marker='v', ls='-', c='red', lw=2)
plt.plot(SH3.Point, SH3.Fdust, marker='v', ls='--', c='red', lw=2)
# 장마
plt.plot(SR1.Point, SR1.Fdust, marker='^', ls=':', c='lightsalmon', lw=2)
plt.plot(SR2.Point, SR2.Fdust, marker='^', ls='-', c='lightsalmon', lw=2)
plt.plot(SR3.Point, SR3.Fdust, marker='^', ls='--', c='lightsalmon', lw=2)

# 가을
# 미세먼지
plt.plot(AD1.Point, AD1.Fdust, marker='v', ls=':', c='mediumpurple', lw=2)
plt.plot(AD2.Point, AD2.Fdust, marker='v', ls='-', c='mediumpurple', lw=2)
plt.plot(AD3.Point, AD3.Fdust, marker='v', ls='--', c='mediumpurple', lw=2)
# 일교차
plt.plot(AT1.Point, AT1.Fdust, marker='^', ls=':', c='orchid', lw=2)
plt.plot(AT2.Point, AT2.Fdust, marker='^', ls='-', c='orchid', lw=2)
plt.plot(AT3.Point, AT3.Fdust, marker='^', ls='--', c='orchid', lw=2)

# 겨울
# 한파
plt.plot(WC1.Point, WC1.Fdust, marker='v', ls=':', c='blue', lw=2)
plt.plot(WC2.Point, WC2.Fdust, marker='v', ls='-', c='blue', lw=2)
plt.plot(WC3.Point, WC3.Fdust, marker='v', ls='--', c='blue', lw=2)
# 눈
plt.plot(WS1.Point, WS1.Fdust, marker='^', ls=':', c='lightsteelblue', lw=2)
plt.plot(WS2.Point, WS2.Fdust, marker='^', ls='-', c='lightsteelblue', lw=2)
plt.plot(WS3.Point, WS3.Fdust, marker='^', ls='--', c='lightsteelblue', lw=2)

# plt.legend(['봄 미세먼지 5/5','봄 미세먼지 5/6','봄 미세먼지 5/7', '봄 일교차 5/2','봄 일교차 5/3','봄 일교차 5/4',
#             '여름 더위 8/4', '여름 더위 8/5', '여름 더위 8/6', '여름 장마 7/1','여름 장마 7/2','여름 장마 7/3',
#             '가을 미세먼지 9/16', '가을 미세먼지 9/17', '가을 미세먼지 9/18', '가을 일교차 9/13','가을 일교차 9/14','가을 일교차 9/15',
#             '겨울 한파 1/26', '겨울 한파 1/27', '겨울 한파 1/28', '겨울 눈 1/29','겨울 눈 1/30','겨울 눈 1/31'])

plt.xlabel('Time Point')
plt.ylabel('미세먼지\n')
plt.title('미세먼지 - Case8\n', fontsize=15)

plt.show()