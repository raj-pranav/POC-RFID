import logging
from pathlib import Path

def setup_log(folder: Path):
    logging.basicConfig(filename= folder / 'RFID.log',
                        level = logging.DEBUG,
                        filemode = 'w',
                        format = "{asctime:s} [{name:^15s}]  [{levelname:^8s}] | [{message:s}]",
                        style='{',
                        datefmt = '%d-%b-%y %H:%M:%S')
    
    print ('Logging setup Successful !')