import sqlite3
from pathlib import Path
import os
import logging
import logging_setup

source_dir = Path(r'C:\PRANAVRAJ\IP_Docs\My_Work_MBRDI\Blockchain-RFIDTag_partIdentification\code\src')
os.chdir(source_dir)

log = logging.getLogger('RFID.DB')
log.info('Data base created ..') 
conn = sqlite3.connect('verified_tags.db')
conn.execute(''' CREATE TABLE IF NOT EXISTS RFID_TAGS
            (VIN INT PRIMARY KEY NOT NULL,
            rfid    TEXT    NOT NULL,
            name    TEXT    NOT NULL);
            ''')

      
conn.close()