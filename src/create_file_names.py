## This will be for creating my file names and using them 
## This will be imported into main


class Filenames:
    def __init__(self ,  dir ):
        self.dir = dir
    def create_dir_variables(self):
        self.transcend_dir = self.dir + "Data\\Raw\\Transcend-data\\"
        self.smartctl_dir = self.dir + "Data\\Raw\\Smartctl\\"
        self.chassis_ssd_xlsx = self.dir + "Data\\Raw\\Locus-Chassis-SSD.xlsx"
        self.processed_csv = self.dir + "Data\\Processed\\collected_data.csv"
