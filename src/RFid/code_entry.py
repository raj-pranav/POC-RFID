from code import interact
from os import getcwd
from pathlib import Path
import logging

from RFid.logging_setup import setup_log
from RFid.pi_board.DB import create_tables, update_PREV_VEH_STATE, update_RFID_TAGS, read_prev_Tags, discover_name_from_tag
from RFid.pi_board.file_handlers import read_prev_data, read_tags_record, read_curr_tags

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

# Read rfid from environment
Tags_detected = read_curr_tags(source_dir)
print (f'Currently scanned tags: {Tags_detected}')

# Read all Tags from previous vehicle state
prev_tags = read_prev_Tags(source_dir)
log.info(f'Previously available Tags: {prev_tags}')
# print (f'Previous Tags: {prev_tags}')

# compare the tags value
missing_cntr = 0
for tag in Tags_detected:
    if tag not in prev_tags:
        missing_cntr += 1
        print (f'Missing Tag Alert !!  <<{tag}>> is a new UN-identified Tag')
    # else:
    #     print ('Same as Previous')

# Find missing tags (which was previously assembled)
if missing_cntr > 0:
    missing_org_tag = set(prev_tags) - set(Tags_detected)
    miss_tag = str(list(missing_org_tag)[0])
    log.info(f'Missing tags: {miss_tag}')
    discover_name_from_tag(source_dir, miss_tag) # Get the Part name of the tag
else:
    print ('Yieee !! All Genuine parts are present ')





#
