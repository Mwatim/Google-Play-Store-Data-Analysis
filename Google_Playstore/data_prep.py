# import requisite data processing packages
import pandas as pd

def data_prep(data):
    """
    Function to clean and prepare the dataset for the analysis process
    """
    # read the csv file into a dataframe
    df = pd.read_csv(data)

    # clean the Installs column in prep for analysis 
    df['Installs'] = df['Installs'].str.replace('[^\d]', '', regex=True)

    # coerce the resultant output to csv format
    df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')

    # clean the Android Ver column 
    df['Android Ver'] = df['Android Ver'].str.replace(' and up', '')

    # drop NaN/NULL values
    df.dropna()

    # create the placeholder for the filename
    desired_file_name = 'cleaned_googleplaystore.csv'

    # save the df to the csv file
    df.to_csv(desired_file_name, index=False)

    print("Successful operation")

    return "Data cleaning and preparation completed successfully."