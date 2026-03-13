### This is the main execution file for Locus SSD Mining/Plotting Data

import csv
from pathlib import Path
from src.create_file_names import Filenames
import src.get_serial_numbers as gsn
import src.get_transcend_data as gtn

if __name__ == "__main__":
    print("Collecting data....")
    dir = __file__[:-7] ## get rid of main.py
    
    ## create the file names
    file = Filenames(dir)
    file.create_dir_variables()

    ## collect the chassis and serial number first
    gsn.get_serial_numbers_main(file)

    ## collect the imformation from transcend data
    gtn.get_transcend_data_main(file)

    
    