import pandas as pd
import numpy as np

#df = pd.read_csv("20data.csv")


# it will print top 5 rows and columns
#print(df.head())


# it will print information of table about total, column
#print(df.info())

## it will print mean, count, avg of table
#print(df.describe())

## celaning missing value

# counting isnull value in each column

# print(df.isnull().sum())

## adding value into null/ missing value into Age column

'''
df["Age"] = df["Age"].fillna(df["Age"].mean())
print(df.isnull().sum())



# adding missing value to Marks with avg value
df["Marks"] = df["Marks"].fillna(df["Marks"].median())
print(df.isnull().sum())

print(df.head())

## adding missing value to city with existing & repeating

df["City"] = df["City"].fillna(df["City"].mode()[0])
print(df.isnull().sum())

'''
## changint varchar value in null value with mode unique

# print(df.duplicated().sum())

#to drop duplicate data

# df = df.drop_duplicates()

## removing the extra speaces

'''

df["Name"] = df["Name"].str.strip()
df["City"] = df["City"].str.strip()

print(df.info())

'''


## strandardize text converting proper fromat

#df["City"] = df["City"].str.title()
#df.info()


## replacing invalid value in this case age

#applying condition for valid range of data


'''
check value and replace with nan

invalid_age = df[(df["Age"] < 0  | (df["Age"] > 100))]
#df.loc[df["Age"] < 0, "Age"] = np.nan  #OR
df.loc[df["Age"] < 0, "Age"] = 20
print(invalid_age)
print(df.describe())

'''

#for the age if it alue not availavle repace with nan(most common case)




#df.replace(["N/A", "NULL", "?"], np.nan, inplace=True)  #i choose nan beacuse -1 represnt missing

'''
# if want value so add value

df.loc[df["Age"] < 0, "Age"] = np.nan


'''

#checking for data in marks conditions

'''

invalid_marks = df[(df["Marks"] < 0) | (df["Marks"] > 100)]

print(invalid_marks)

# changing or fill data with avg, mean, median

df.loc[df["Marks"] > 100, "Marks"] = df["Marks"].median()
print(df.describe())

df["Age"] = df["Age"].round().astype(int)
df["Marks"] = df["Marks"].astype(int)

df.to_csv("20Cleandata", index = False)

'''

## replacing column name


'''
df.rename(columns={"age":"AGE"}, inplace=True)

'''

## converting to integer(No Decimal)
'''

df["Age"] = df["Age"].astype(int)

'''

## Keeping data as decimal but display as whole number

'''
print(df.round(0))

OR

df["Age"] = df["Age"].round().astype(int)

'''

## Remove the entire row

'''
df = df[df("Marks") <= 100]

OR 

df = df.drop(df[df["Marks"] > 100].index)

'''


                             ## cleaning 100 data

df = pd.read_csv("bad100.csv")

#print(df.head())

'''print(df.info())

print(df.dtypes)
print(df.isnull().sum())'''


#print(df.head())

#print(df.duplicated().sum())



print(df["Salary"].unique())

#print(df["Salary"].value_counts())  #here finds the salary is negative -5000, nan and abc

#filling nan salary with value
#print(df.describe())

#change any text into numeric

'''

df["Salary"] = df["Salary"].replace("abc", np.nan)

#df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
print(df["Salary"].value_counts())

print(df["Salary"].unique())

#change negative value into positive
df["Salary"] = df["Salary"].replace("-5000", 5000)
print(df["Salary"].unique())

#change its type from object to numeric

df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")
print(df.info())

print(df.dtypes)

'''

'''

#after changing abc to nan fill nan with value

df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
df["Salary"] = df["Salary"].astype(int)
print(df["Salary"].unique())

'''

#end of data cleaning of salary



#begain of name column

'''
print(df["Name"].unique())  #finding nan on name field

#filling nan with values

df["Name"] = df["Name"].fillna(df["Name"].mode()[0])
print(df["Name"].unique())

df["Name"] = df["Name"].str.strip()

'''
#end of data cleaning and filling missing values in Name column



print(df.info())


'''

# changing metadata of date column from object to date

print(df["Date"].unique())

# converting into date

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

print(df["Date"].dtypes)

#changing to format od Year, monts, day

df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")
print(df.head(10))

#filling unknown data with ffill or bfill
df["Date"] = df["Date"].ffill()


'''


'''
# Now full and finall checking for Address

print(df.isnull().sum())
print(df["Address"].unique()) #find missing value

df["Address"] = df["Address"].replace([" ", "nan", ""], np.nan)
print(df["Address"].unique())



df["Address"] = df["Address"].fillna("Unknown")
print(df["Address"].unique())

df["Address"] = df["Address"].str.replace("Kathmndu", "Kathmandu", case=False, regex=False)
print(df["Address"].unique())
print(df.info())


'''

print(df.dtypes)

print(df["Date"].head())

#no duplicate data is being remvved from bad100 data
'''

# saving data
df.to_csv("Clean_100_Data", index=False)


'''