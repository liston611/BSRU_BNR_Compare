import pandas as pd
import os

#Find bus stops that will not have change to route names, EOLs, numbers.


#Build table of stops w/ route & EOL
#Import table of stops from BNR from Remix by prompting user

current_directory = os.getcwd()
#file_path = os.path.join(current_directory,'BNR_EOL.csv')
file_path = 'BNR_EOL.csv'


# Check if the file exists before reading it
if os.path.exists(file_path):
    # For example, using Pandas to read a CSV file
    df = pd.read_csv(file_path)
    print("File loaded successfully!")
    # Perform operations on the DataFrame 'df'
    # For instance, display the first few rows:
    print(df.head())
else:
    print("File not found in the current directory.")