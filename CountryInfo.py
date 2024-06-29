import pandas as pd 
country = pd.read_csv(r"C:\Users\jto07\Python-projects\countries.csv",)
country = country.drop(columns = "Pop. Density (per sq. mi.)")
country = country.drop(columns = "Area (sq. mi.)")
country = country.drop(columns = "Other (%)")
country = country.drop(columns = "Net migration")
country = country.drop(columns = "Infant mortality (per 1000 births)")
country = country.drop(columns = "Literacy (%)")
country = country.drop(columns = "Phones (per 1000)")
country = country.drop(columns = "Arable (%)")
country = country.drop(columns = "Crops (%)")
country = country.drop(columns = "Climate")
country = country.drop(columns = "Birthrate")
country = country.drop(columns = "Deathrate")
country = country.drop(columns = "Agriculture")
country = country.drop(columns = "Industry")
country = country.drop(columns = "Service")
print('What country do you like to know?')
coun = input() + ' '
index = country.index[country['Country']==coun].tolist()
info = country.loc[index]
if index == []:
    print('The country do not exist')
else:
    print(info)