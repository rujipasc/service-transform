import pandas as pd
import datetime

file_read = r"D:\Users\chrujipas\Desktop\next-project\foundation-clean\Extract-Zip\Position.csv"

# Load data and skip the first row
df = pd.read_csv(file_read, skiprows=1, low_memory=False)  # added low_memory=False to suppress warning

# Convert Start Date to datetime format
df['Start Date'] = pd.to_datetime(df['Start Date'], errors='coerce')
df.dropna(subset=['Start Date'], inplace=True)  # drops the rows where date conversion failed

# Sort by the Start Date in datetime format
df.sort_values(by=['Start Date'], ascending=False, inplace=True)

# Convert sorted dates back to string format
df['Start Date'] = df['Start Date'].dt.strftime('%m/%d/%Y')

# Desired date format
date_format = '%m/%d/%Y'  # Adjusted format to match the strftime above

# Validate the Start Date column format
try:
    # Use apply to check each date
    df['Start Date'].apply(lambda x: datetime.datetime.strptime(x, date_format))
    print("All dates are in the correct format!")
    df['Start Date'].to_csv(r"D:\Users\chrujipas\Desktop\next-project\foundation-clean\valiate-date.csv", encoding='utf-8', index=False)  # added index=False to avoid saving row numbers
except ValueError:
    print("Incorrect data format, should be MM/DD/YYYY")
