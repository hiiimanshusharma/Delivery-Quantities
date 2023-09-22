from nsedt import equity as eq
from datetime import date
import time

import pandas as pd

companies = pd.read_csv(r"C:\Users\91830\Downloads\MCAP31032023_0 - Sheet1 - MCAP31032023_0 - Sheet1.csv")
print(companies.head())
symbols = companies['Symbol'].tolist()
print(symbols)

start_date = date(2011, 1, 1)
end_date = date(2023, 6, 30)

df = pd.DataFrame()  # Initialize an empty DataFrame

for s in symbols:
    retries = 3  # Number of retries in case of exception
    while retries > 0:
        try:
            price_df = eq.get_price(start_date, end_date, symbol=s)
            price_df[s] = s  # Add a column with value s to the DataFrame
            df = df.append(price_df)
            break  # Exit the loop if data retrieval is successful
        except Exception as e:
            print(f"Error retrieving data for symbol {s}: {e}")
            retries -= 1
            if retries > 0:
                print("Retrying in 5 sec...")
                time.sleep(5)  # Wait for 1 minute before retrying
            else:
                print("Maximum retries reached. Moving to the next symbol.")

df.to_excel('delivery.xlsx',index=False)
print(df)