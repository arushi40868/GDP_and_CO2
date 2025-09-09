import pandas as pd

link = 'https://github.com/nickeubank/MIDS_Data/raw/refs/heads/master/World_Development_Indicators/wdi_small_tidy_2015.csv'

df = pd.read_csv(link)

pulled = df[['Country Name', 'Mortality rate, infant (per 1,000 live births)', 'GDP per capita (constant 2010 US$)']]

print(pulled)