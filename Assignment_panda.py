# *** Question 1 ***
import pandas as pd
import os
new_dataframe = pd.DataFrame(
    {
        "name" : ['Ekankshi', 'Garima','Parth', 'Nandini', 'Shiven'],
        "age" : ['20', '19','18', '18', '17'],
        "mail_id" : ['ekankshi@gmail.com', 'garima@gmail.com','parth@gmail.com', 'nandini@gmail.com', 'shiven@gmail.com'],
        "phone_no" : [123,456,789,357,246],
    }
)
print(new_dataframe)



# *** Question 2 ***
import pandas as pd
import os
df=pd.read_csv('weather.csv.txt')
print(type(df))
print(df.head(5))       #First 5 rows of Dataframe
print(df.head(10))      #First 10 rows of Dataframe
# basic statistics
mean = df['MinTemp'].mean()
print(mean)
desc = df['MinTemp'].describe()
print(desc)
min = df['MinTemp'].min()
print(min)
max = df['MinTemp'].max()
print(max)
mode = df['MinTemp'].mode()
print(mode)
median = df['MinTemp'].median()
print(median)

print(df.tail(2))          # Last 5 rows of dataset
a = df.iloc[:,2]
print(a)                    # second column extraction
mean = df['MinTemp'].mean()
print(mean)
desc = df['MinTemp'].describe()
print(desc)
min = df['MinTemp'].min()
print(min)
max = df['MinTemp'].max()
print(max)
mode = df['MinTemp'].mode()
print(mode)
median = df['MinTemp'].median()
print(median)



