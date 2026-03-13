## This will be for mining the data out of the transcend smart data

## IMPORTS

import pandas as pd
from pathlib import Path

class data_to_be_written():
    def __init__(self):
        self.headers = None
        self.dict = {}
    
    def add_to_dictionary(self , serial_number , data ):
        self.dict[serial_number] = data
    
def write_to_csv( df , File , SSD_sn_list , SSD_data ):
    ## add the headers
    for header in SSD_data.headers:
        df[header] = ""
    
    ## now add the row by finding the serial number and adding the data that way
    for serial in SSD_sn_list:
        df.loc[df['SSD Serial No.'] == serial, SSD_data.headers] = SSD_data.dict[serial]

    
    df.to_csv(File.processed_csv , index=False)

def parse_data( serial_number_file , serial_number , SSD_data ):
    ## first time writing
    if not SSD_data.headers:
        SSD_data.headers = [ 
                            'Power-On Hours' , 
                            'Valid Blocks' , 
                            'Life Percentage' , 
                            'CRC',
                            'Total LBA Written'
                            ]
    column_names = ['Code', 'Attribute' , 'Value'] ## to skip past bad rows
    df_sn = pd.read_csv(serial_number_file , names=column_names, header=None, engine='python')
    ## let us get each value needed and append it to data
    data = []
    data.append(str(df_sn.iloc[9 , 2])) ## Power on hours
    data.append(str(df_sn.iloc[17 , 2])) ## Valid Blocks
    data.append(str(df_sn.iloc[24 , 2])) ## Remaining Life
    data.append(str(df_sn.iloc[32 , 2])) ## CRC count
    data.append(str(df_sn.iloc[34 , 2])) ## Total LBA written

    ## add to the dictionary
    SSD_data.add_to_dictionary(serial_number , data )



def get_transcend_data_main( File ):
    ## get the SSD serial numbers
    df = pd.read_csv(File.processed_csv) 
    SSD_sn_list = df['SSD Serial No.'].values

    ## cycle through the Transcend data dir
    directory_path = Path(File.transcend_dir)

    ## will be use to writing to csv later
    SSD_data = data_to_be_written()

    ## Cycle through the directory, if the serial number exists send to parse data
    ## if not print the serial number does not exist
    for item in directory_path.iterdir():
        if item.stem in SSD_sn_list:
            parse_data(item , item.stem, SSD_data)
        else:
            print(item.stem , "not in spreadsheet")
        
    write_to_csv(df , File ,SSD_sn_list , SSD_data )