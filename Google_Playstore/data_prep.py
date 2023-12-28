# import requisite data processing packages
import os
import logging
import pandas as pd


def configure_logging():
    """
    Function to configure logging functionality
    """
    # Create a stream handler and set the level to INFO
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Create a formatter and attach it to the handler
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )
    console_handler.setFormatter(formatter)

    # Get the root logger and add the console handler
    logger = logging.getLogger()
    logger.addHandler(console_handler)
    logger.setLevel(logging.INFO)

    # Propagate the level to all loggers
    logging.root.setLevel(logging.INFO)


configure_logging()


def sizeof_fmt(num, suffix="B"):
    """
    Function to format file size.

    Parameters:
    - num (int): the file size

    Returns:
    -str: Formatted output
    """
    for unit in ("", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"):
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"


def data_prep(data):
    """
    Function to prepare the dataset for analysis

    Parameters:
    - data (str): Path to the CSV file.

    Returns:
    - pd.DataFrame: Cleaned DataFrame.
    - str: Success/Error message.
    """
    try:
        # read the csv file into a dataframe
        df = pd.read_csv(data)
        logging.info(
            f"Acquired {os.path.basename(data)} file. Size: {sizeof_fmt(os.path.getsize(data))}."
            f"Starting data cleaning."
        )

        # clean the Installs column in prep for analysis
        df["Installs"] = df["Installs"].str.replace("[^\d]", "", regex=True)

        # coerce the resultant output to csv format
        df["Installs"] = pd.to_numeric(df["Installs"], errors="coerce")

        # clean the Android Ver column
        df["Android Ver"] = df["Android Ver"].str.replace(" and up", "")

        # drop NaN/NULL values
        df.dropna()

        # create the placeholder for the filename
        desired_file_name = "cleaned_googleplaystore.csv"

        # save the df to the csv file
        df.to_csv(desired_file_name, index=False)

        logging.info("Data cleaning and preparation completed successfully.")
        print("Data cleaning and preparation completed successfully.")
        return df

    except Exception as e:
        logging.error(f"Error during data preparation: {e}")
        print(f"Error during data preparation: {e}")
        return None


# Usage
data_prep("path_to_your_file")
