import pandas as pd
df = pd.read_csv("grains.csv")

#Q1.Print all the data of the data set
print(df)

#Q2.Print all the state and district columns
print('\n',df[["state","district"]])

#Q3.Print all the varieties of vegetables
print('\n',df["variety"])

#Q4.Print max modal_price
print('\n',df["modal_price"].max())

#Q5.Print sum of max_price
print('\n',df["max_price"].sum())

#Q6.Print average max_price
print('\n',df["max_price"].sum()/len(df["max_price"]))

#Q7.Print average modal_price
print('\n',df["modal_price"].sum()/len(df["modal_price"]))

#Q8.Print top 10 records
print('\n',df.head(10))

#Q8.Print bottom 10 records
print('\n',df.tail(10))

#Q9.Print all the data at even indexing position
print('\n',df.iloc[::2])

#Q10.Print all the data at odd indexing position
print('\n',df.iloc[1::2])

#Q11.Print all the state names stored at even indexing position
print('\n',df.iloc[::2,0])

#Q12.Print all the markets stored at odd indexing postions
print('\n',df.iloc[1::2,2])

#Q13.Print the arrival_dates and min_price stored at even position
print('\n',df.iloc[::2,5:7])

#Q14.Print all the entries of the state of Andaman and nicobar
print('\n',df[df["state"]=="Andaman and Nicobar"])

#Q15.Print max_price greater than 10k
print('\n',df[df['modal_price']>=10000])

#Q16.Print modal_price greater than 5k and variety tomato
print("\n",(df[(df["modal_price"]>=5000) & (df["variety"]=="Onion")]))

#Q17.Print all the count of the states
print('\n',df.groupby("state").count())

#Q18.Print rows 1-20
print('\n',df.iloc[1:21])

#Q19.Print the data on 100th row
print('\n',df.iloc[100])

#Q20.Sort the data in descending order on the basis of modal_sales
print('\n',df.sort_values(by=["modal_price"],ascending=[False]))