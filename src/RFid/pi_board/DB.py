import sqlite3
import logging
from pathlib import Path

log = logging.getLogger('RFid.DB')

DB_NAME = 'verified_tags.db'


def create_tables(location: Path):
    log.info('Creating/Updating Tables ..')

    conn = sqlite3.connect(Path(location) / DB_NAME)
    cur = conn.cursor()

    cur.execute(''' CREATE TABLE IF NOT EXISTS RFID_TAGS (
                    rfid_tag TEXT PRIMARY KEY NOT NULL,
                    part_name   TEXT  NOT NULL,
                    VIN TEXT NOT NULL ) ''')     
    
    cur.execute(""" CREATE TABLE IF NOT EXISTS PREV_VEH_STATE (
                    VIN TEXT,
                    Tags TEXT PRIMARY KEY NOT NULL,
                    name TEXT ) """)

    conn.commit()
    print ('Tables created successfully !!')

    conn.close()
    

# Inserting data in PREV_VEH_STATE table
def update_PREV_VEH_STATE(location, values):
    conn = sqlite3.connect(Path(location) / DB_NAME)
    cur = conn.cursor()

    log.info(f'added values to PREV_VEH_STATE table: {values}')
    cur.executemany("INSERT OR IGNORE INTO PREV_VEH_STATE VALUES (?,?,?)", values)

    conn.commit()
    print ('Data successfully added to table: PREV_VEH_STATE !')
    conn.close()

# Insert data in RFID_TAGS table
def update_RFID_TAGS(location, values):
    conn = sqlite3.connect(Path(location) / DB_NAME)
    cur = conn.cursor()

    log.info(f'added values to RFID_TAGS table: {values}')
    cur.executemany("INSERT OR IGNORE INTO RFID_TAGS VALUES (?,?,?)", values)

    conn.commit()
    print ('Data successfully added to table: RFID_TAGS !')
    conn.close()


def read_prev_Tags(location):

    output = []
    conn = sqlite3.connect(Path(location) / DB_NAME)
    cur = conn.cursor()

    cur.execute("SELECT Tags from PREV_VEH_STATE")
    tags = cur.fetchall()

    for tag in tags:
        output.append(tag[0])

    conn.close()

    return output

    
def discover_misplaced_tag(location, tag:str, uT):

    conn = sqlite3.connect(Path(location) / DB_NAME)
    cur = conn.cursor()

    cur.execute("SELECT rfid_tag, part_name from RFID_TAGS WHERE rfid_tag = ?", (tag,))
    _name = cur.fetchall()

    log.info(f'{_name} was Orginal part, has been misplaced by {uT} !!')
    
    print (f'{_name} >> has been Misplaced by {uT} !!')

    conn.close()


def discover_missing_tag(location, tag:str):

    conn = sqlite3.connect(Path(location) / DB_NAME)
    cur = conn.cursor()

    cur.execute("SELECT rfid_tag, part_name from RFID_TAGS WHERE rfid_tag = ?", (tag,))
    _name = cur.fetchall()

    log.info(f'{_name} -> missing from vehicle !')
    
    print (f'{_name} -> missing from vehicle !')

    conn.close()

    # Make change permanent and close db connection
    # conn.commit()
    # conn.close()
