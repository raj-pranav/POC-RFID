import sqlite3
import logging
from pathlib import Path

log = logging.getLogger('RFid.DB')

DB_NAME = 'verified_tags.db'

def update_db(location: Path):
    log.info('Creating/Updating Database ..')

    conn = sqlite3.connect(Path(location) / DB_NAME)
    conn.execute(''' CREATE TABLE IF NOT EXISTS RFID_TAGS
                (VIN INT PRIMARY KEY NOT NULL,
                rfid_tag    TEXT    NOT NULL,
                part_name    TEXT    NOT NULL);
                ''')     
    conn.close()


# There will be another table , which stores the previous configuration of the car e.g- parts name with rfid tag