import logging
from pathlib import Path
import os

source_dir = Path(r'C:\PRANAVRAJ\IP_Docs\My_Work_MBRDI\Blockchain-RFIDTag_partIdentification\code\src')
os.chdir(source_dir)

logging.basicConfig(filename='RFID.log',
                    level = logging.DEBUG,
                    filemode = 'w',
                    format = "{asctime:s} [{name:^15s}]  [{levelname:^8s}] | [{message:s}]",
                    style='{',
                    datefmt = '%d-%b-%y %H:%M:%S')