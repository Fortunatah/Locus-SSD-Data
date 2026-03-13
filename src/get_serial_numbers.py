## This will be for collecting the serial numbers from the spreadsheet
## This will collect the data of the two and write it to the spreadsheet

## IMPORTS

import pandas as pd
import os

def get_serial_numbers_main( File ):
    df = pd.read_excel(File.chassis_ssd_xlsx)

    ##if the csv file exists, we want to start from scratch
    if os.path.exists(File.processed_csv):
        os.remove(File.processed_csv)

    ## subset only the first two columns
    df_subset = df[['Chassis Serial No.' , 'SSD Serial No.']]

    ## write to csv
    df_subset.to_csv(File.processed_csv , index=False)

