import pandas as pd

Report = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/7.Report_Final.csv')
Fdust = pd.read_csv('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/7.Fdust_Final.csv')


df = Report
# df = Fdust
df_row = df.shape[0]

#
i = 0
spring_dust = []
spring_temp = []
summer_heat = []
summer_rain = []
autumn_dust = []
autumn_temp = []
winter_cold = []
winter_snow = []


for i in range(df_row) :
    if df.iloc[i,1] == '2017-05-05' :
        spring_dust.append(df.iloc[i,:])
    elif df.iloc[i,1] == '2017-05-06' :
        spring_dust.append(df.iloc[i,:])
    elif df.iloc[i,1] == '2017-05-07' :
        spring_dust.append(df.iloc[i,:])
#---------------------------------------
    elif df.iloc[i,1] == '2017-05-02' :
        spring_temp.append(df.iloc[i,:])
    elif df.iloc[i,1] == '2017-05-03' :
        spring_temp.append(df.iloc[i,:])
    elif df.iloc[i,1] == '2017-05-04' :
        spring_temp.append(df.iloc[i,:])
#---------------------------------------
    elif df.iloc[i,1] == '2017-08-04' :
        summer_heat.append(df.iloc[i,:])
    elif df.iloc[i,1] == '2017-08-05' :
        summer_heat.append(df.iloc[i,:])
    elif df.iloc[i,1] == '2017-08-06' :
        summer_heat.append(df.iloc[i,:])
#---------------------------------------
    elif df.iloc[i,1] == '2017-07-01' :
        summer_rain.append(df.iloc[i,:])
    elif df.iloc[i,1] == '2017-07-02' :
        summer_rain.append(df.iloc[i,:])
    elif df.iloc[i,1] == '2017-07-03' :
        summer_rain.append(df.iloc[i,:])
#---------------------------------------
    elif df.iloc[i,1] == '2017-09-16' :
        autumn_dust.append(df.iloc[i,:])
    elif df.iloc[i,1] == '2017-09-17' :
        autumn_dust.append(df.iloc[i,:])
    elif df.iloc[i,1] == '2017-09-18' :
        autumn_dust.append(df.iloc[i,:])
#---------------------------------------
    elif df.iloc[i,1] == '2017-09-13' :
        autumn_temp.append(df.iloc[i,:])
    elif df.iloc[i,1] == '2017-09-14' :
        autumn_temp.append(df.iloc[i,:])
    elif df.iloc[i,1] == '2017-09-15' :
        autumn_temp.append(df.iloc[i,:])
#---------------------------------------
    elif df.iloc[i,1] == '2017-01-26' :
        winter_cold.append(df.iloc[i,:])
    elif df.iloc[i,1] == '2017-01-27' :
        winter_cold.append(df.iloc[i,:])
    elif df.iloc[i,1] == '2017-01-28' :
        winter_cold.append(df.iloc[i,:])
#---------------------------------------
    elif df.iloc[i,1] == '2017-01-29' :
        winter_snow.append(df.iloc[i,:])
    elif df.iloc[i,1] == '2017-01-30' :
        winter_snow.append(df.iloc[i,:])
    elif df.iloc[i,1] == '2017-01-31' :
        winter_snow.append(df.iloc[i,:])


spring_dust = pd.DataFrame(spring_dust)
spring_temp = pd.DataFrame(spring_temp)
summer_heat = pd.DataFrame(summer_heat)
summer_rain = pd.DataFrame(summer_rain)
autumn_dust = pd.DataFrame(autumn_dust)
autumn_temp = pd.DataFrame(autumn_temp)
winter_cold = pd.DataFrame(winter_cold)
winter_snow = pd.DataFrame(winter_snow)


spring_dust = spring_dust[spring_dust.Point != 0]
spring_temp = spring_temp[spring_temp.Point != 0]
summer_heat = summer_heat[summer_heat.Point != 0]
summer_rain = summer_rain[summer_rain.Point != 0]
autumn_dust = autumn_dust[autumn_dust.Point != 0]
autumn_temp = autumn_temp[autumn_temp.Point != 0]
winter_cold = winter_cold[winter_cold.Point != 0]
winter_snow = winter_snow[winter_snow.Point != 0]


spring_dust.to_csv('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/spring_dust.csv')
spring_temp.to_csv('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/spring_temp.csv')
summer_heat.to_csv('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/summer_heat.csv')
summer_rain.to_csv('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/summer_rain.csv')
autumn_dust.to_csv('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/autumn_dust.csv')
autumn_temp.to_csv('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/autumn_temp.csv')
winter_cold.to_csv('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/winter_cold.csv')
winter_snow.to_csv('C:/Users/DAIN/환경설비팀요청자료2/for_대합실미세먼지/winter_snow.csv')


# spring_dust.to_csv('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/spring_dust.csv')
# spring_temp.to_csv('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/spring_temp.csv')
# summer_heat.to_csv('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/summer_heat.csv')
# summer_rain.to_csv('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/summer_rain.csv')
# autumn_dust.to_csv('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/autumn_dust.csv')
# autumn_temp.to_csv('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/autumn_temp.csv')
# winter_cold.to_csv('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/winter_cold.csv')
# winter_snow.to_csv('C:/Users/DAIN/환경설비팀요청자료2/for_터널미세먼지/winter_snow.csv')

