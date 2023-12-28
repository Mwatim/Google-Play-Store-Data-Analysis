# import requisite data processing packages
import logging
import pandas as pd

def data_prep(data):
    """
    Function to clean and prepare the dataset for the analysis process.

    Parameters:
    - data (str): Path to the CSV file.

    Returns:
    - pd.DataFrame: Cleaned DataFrame.
    - str: Success message.
    """
    try:
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

        logging.info("Data cleaning and preparation completed successfully.")
        return df, "Data cleaning and preparation completed successfully."

    except Exception as e:
        logging.error(f"Error during data preparation: {e}")
        return None, f"Error during data preparation: {e}"

# logging
logging.basicConfig(level=logging.INFO) 

# Example usage:
result_df, result_message = data_prep(r"C:\Users\DELL\Desktop\Appdataprocess\googleplaystore.csv")

print("result_message")
