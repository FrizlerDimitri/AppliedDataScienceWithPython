import numpy as np
import pandas as pd

#Activity 1 - Convert DataFrame¶
#Using the test_assignment_data.csv file locate in the data folder.

# Task 1 - Lets say we are only interested in population (POP) and total GDP (tcgdp),
# convert the data frame with “country” as index and POP, tcgdp are columns.

# Task 2 - Rename POP -> Population and tcgdp-> Total GDP
# Task 3 - Add a new column 'GDP Percap’ to the existing data frame.

#Country	POP	TCGDP
#0	Argentina	37335.653	295072.218690
#1	Australia	19053.186	541804.652100
#HINT: GDP per capita can be calculated as ratio of Total GDP and Population.

def activity1(source_path):
    df = pd.read_csv(source_path)
    #print(df[["country", "POP", "tcgdp"]])

    df1=df.rename(columns={"POP":"Population", "tcgdp" : "Total GDP" })
    #print(df1[["country", "Population", "Total GDP"]])

    df2=df1
    df2["GDP Percap"]=df1["Total GDP"]/df1["Population"]

    print(df2[["country", "Population", "Total GDP","GDP Percap"]])
    #print(df1[["country", "Population", "Total GDP","GDPPercap"]])



#Activity 2 - Find Data
#Using the forest fire data “forestfires.csv” and “ReadMe_forestfire.txt” under the datafolder.

#Find the month and day where “rain” measurement is NOT Zero.
#Find the descriptive statistics of “temp” and “wind”.
#Find mean temperature for each month and plot it.
#Find the month and day with the highest and lowest temperature.
#Find the mean temperature at different unique locations (x,y).






def activity2(source_path):
    df = pd.read_csv(source_path)

    #Task 1
    m_and_day_not_zero = df.loc[df["rain"] != 0]
    m_and_day_not_zero_result=m_and_day_not_zero[["month", "day"]]
    #print(m_and_day_not_zero_result)

    #Task 2

    describe_temp_wind=df.describe()[["temp","wind"]]
    #print(describe_temp_wind)

    #Task 3
    temp_mean_for_mothes=df.groupby("month").mean()["temp"]
    #print(temp_mean_for_mothes)


    # Task4
    heighest_temp= df.sort_values("temp")[["month","day","temp"]].tail(1)
    lowest_temp=df.sort_values("temp")[["month","day","temp"]].head(1)
    #print(heighest_temp)
    #print(lowest_temp)

    # Task5
    xy_temp_mean= df.groupby(["X","Y"]).mean()["temp"]
    print(xy_temp_mean)
