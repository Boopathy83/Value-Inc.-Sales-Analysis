import pandas as pd

# File_name = pd.read_csv('file.csv')  <---- format of CSV
data = pd.read_csv('transaction2.csv')

data = pd.read_csv('transaction2.csv', sep =";")

#Summary of the dataset
data.info()

# Working with calculations
# Defining variables
CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberofItemsPurchased = 6

#Mathematical operations on Tableau

ProfitPerItem = SellingPricePerItem - CostPerItem
ProfitPerTransaction = NumberofItemsPurchased*ProfitPerItem
CostPerTransaction = NumberofItemsPurchased*CostPerItem
SellingPricePerTransaction = NumberofItemsPurchased*SellingPricePerItem

#CostperTransaction Column Calculation
CostPerItem = data['CostPerItem']
NumberofItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction=CostPerItem*NumberofItemsPurchased

# Adding a new column to a data frame

data['CostPerTransaction'] = CostPerTransaction

data['SalesPerTransaction'] = data['NumberOfItemsPurchased'] * data['SellingPricePerItem']

# Profit Calculation
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

# Markup = Profit/CostPrice

data['Markup'] = data['ProfitPerTransaction'] / data['CostPerTransaction']

# Round function (round should be in small-case)

data['Markup'] = round(data['Markup'],2)

# Combining Data Fields

data['MyDate'] = data['Day'].astype(str)+'-'+data['Month']+'-'+data['Year'].astype(str)

#using iloc to view specific columns/rows
data.iloc[3] # Views the 3rd row
data.iloc[0:3] # views 0,1,2 rows
data.iloc[-5:] # views last 5 
data.head(5) # Brings first five rows
data.iloc[4,2] #Brings 4th row and 2nd column

#Using Split keyword
split_col = data['ClientKeywords'].str.split(',',expand = True)
data['ClientAge'] = split_col[0]
data['ClientBusiness'] = split_col[1]
data['ClientContract'] =  split_col[2]

#using replace function
data['ClientAge'] = data['ClientAge'].str.replace("[","")
data['ClientContract'] = data['ClientContract'].str.replace("]","")

# Using the lower function to change item to lowercase
data['ItemDescription'] = data['ItemDescription'].str.lower()

# New dataset
Seasons = pd.read_csv('value_inc_seasons.csv',sep=';')

# Merge dataset
data = pd.merge(data,Seasons,on = 'Month')

# Drop columns
# To drop multiple columns
# data = data.drop('[Day,Date]',axis=1)
data = data.drop('ClientKeywords',axis =1)
data = data.drop('Day',axis=1)
data = data.drop('Month',axis=1)
data = data.drop('Year',axis=1)

# Export into csv
data.to_csv('ValueInc_Cleaned.csv',index = False)























































