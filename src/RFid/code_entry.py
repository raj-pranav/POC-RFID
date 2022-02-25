from code import interact
from os import getcwd
from pathlib import Path
import logging

import sys
sys.path.append('/home/pi/Documents/POC-RFID/src')

from RFid.logging_setup import setup_log
from RFid.pi_board.DB import create_tables, update_PREV_VEH_STATE, update_RFID_TAGS, read_prev_Tags, discover_misplaced_tag, discover_missing_tag
from RFid.pi_board.file_handlers import read_prev_data, read_tags_record, read_curr_tags
from RFid.pi_board.read_rfid import read_live_tags
from RFid.pi_board import buzzer

# Path configuration
PROJECT_PATH = getcwd()
source_dir   = Path(PROJECT_PATH).parent

setup_log(source_dir)

# Logger for this module
log = logging.getLogger('RFID')

log.info(f'PROJECT Path : {PROJECT_PATH}')
log.info(f'Source Path  : {source_dir}')

# Creating DB and tables inside - onetime task
# create_tables(source_dir)

# Read from file & update database
# prev_values = read_prev_data(source_dir)
# update_PREV_VEH_STATE(source_dir, prev_values)

# tags_internal = read_tags_record(source_dir)
# update_RFID_TAGS(source_dir, tags_internal)

# Read all Tags from previous vehicle state
prev_tags = read_prev_Tags(source_dir)
log.info(f'Previously available Tags: {prev_tags}')
# print (f'Previous Tags: {prev_tags}')

# Read rfid from environment
Tags_detected = read_live_tags(20)
# Tags_detected = read_curr_tags(source_dir)

print (f'{len(Tags_detected)} Tags found after Scanning: {Tags_detected}')

# compare the tags value
unknown_tags = []
for tag in Tags_detected:
    if tag not in prev_tags:
        unknown_tags.append(tag)
        print (f'Unknown Tag Alert !!  <<{tag}>> is a new UN-identified Tag')

log.info(f'{len(unknown_tags)} unknown tags detected : >> {unknown_tags}')


# To detect any misplaced tag
if (len(unknown_tags) > 0) and (len(prev_tags) == len(Tags_detected)):
    print ('INFO about misplaced original Tags )')
    misplace_org_tags = list(set(prev_tags) - set(Tags_detected))
    
    sync_uT = 0 # to get value from unknown tag basket
    for m_tag in misplace_org_tags:
        discover_misplaced_tag(source_dir, m_tag, unknown_tags[sync_uT]) # Get the Part name with tag
        sync_uT += 1


# Some of original tag(s) are missing
if (len(unknown_tags) == 0) and (len(prev_tags) > len(Tags_detected)):
    print ('INFO about original missing Tags ...')
    missing_org_tags = list(set(prev_tags) - set(Tags_detected))
    
    for mis_tag in missing_org_tags:
        discover_missing_tag(source_dir, mis_tag)


# for both missing and misplaced
if (len(unknown_tags) > 0) or (len(prev_tags) >= len(Tags_detected)):
    missing_org_tags = list(set(prev_tags) - set(Tags_detected))

    if missing_org_tags == []:
        print ('Yieee !! All Genuine parts are present & unaffected ')
    else:
        print ('INFO on missing/misplace tags ...')
        buzzer.trigger_buz(intensity = 2, duration = 3)

        for mis_tag in missing_org_tags:
            discover_missing_tag(source_dir, mis_tag)


