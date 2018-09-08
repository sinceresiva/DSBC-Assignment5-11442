import pandas as pd
import datetime
from datetime import date
import random

days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

base=date(2015,1,1) #initialize the base date
date_list = [base + datetime.timedelta(days=x) for x in range(0, 365)] #generate the entire 365 dates
business_date_list=[dt for dt in date_list if not dt.strftime("%A").lower()=='saturday' and not dt.strftime("%A").lower()=='sunday'] #filter business days
business_weekdays_list= [dt.strftime("%A").lower() for dt in business_date_list] 
random_numbers_list=[random.randint(1,1000) for dt in business_date_list] #get corresponding random numbers for index

#get the dataframe
bd_dataframe=pd.DataFrame({'weekdays':business_weekdays_list,'business_days':business_date_list,'indexes':random_numbers_list},index=random_numbers_list)
print('********DataFrame is*************')
print(bd_dataframe)

#Sum of values in series for every wednesday
df_weekdays=bd_dataframe.groupby('weekdays').sum()
df_weekdays=df_weekdays.sort_values(['indexes'],ascending=True)
df_wed=df_weekdays.filter(like='wednesday', axis=0)
print('********Sum of values in series for every wednesday:*************')
print(df_wed.head(1))

#average for each calender month
print('********Average for each calender month:*************')
bd_dataframe['business_days'] = pd.to_datetime(bd_dataframe['business_days'])
bd_calendar_datafame = bd_dataframe.groupby(bd_dataframe['business_days'].dt.strftime('%B')).mean()
bd_calendar_datafame = bd_calendar_datafame.sort_values(['indexes'],ascending=True)
print(bd_calendar_datafame)

#For each group of four consecutive calendar months in s, find the date on which the highest value occurred.
print('********The date on which the highest value occurred in group of four consecutive calendar months.:*************')
bd_dataframe["quarter"]=bd_dataframe['business_days'].apply(lambda x: (x.month-1)/4)
bd_dataframe = bd_dataframe.sort_values(by=["quarter","indexes"],ascending=[1,0])
print(bd_dataframe)
bd_df_quarter=bd_dataframe.groupby(bd_dataframe["quarter"]).first()
print(bd_df_quarter)








